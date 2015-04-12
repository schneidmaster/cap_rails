import os, sublime, sublime_plugin

if sublime.version() >= '3000':
  from CapRails.caprails_command import CapRailsCommand
  from CapRails.constants import *
else:
  from caprails_command import CapRailsCommand
  from constants import *

class CapistranoRailsCommand(sublime_plugin.WindowCommand):
  def load_config(self):
    s = sublime.load_settings(SETTINGS_FILE)
    self.command = CapRailsCommand(
      {
        'use_rbenv': s.get('check_for_rbenv'),
        'use_rvm': s.get('check_for_rvm'),
        'rvm_auto_ruby_path': s.get('rvm_auto_ruby_path'),
        'rbenv_path': s.get('rbenv_path')
      }
    )
    self.stages_folder = s.get('stages_folder')

class CapistranoRailsDeployCommand(CapistranoRailsCommand):

  def run(self):

    # Init configuration.
    self.load_config()

    # Locate the project folder.
    project_folder = self.window.folders()[0]

    # Ensure the open folder is a Rails project with Capistrano.
    stages_folder = project_folder + '/' + self.stages_folder
    if not os.path.isdir(stages_folder):
      sublime.message_dialog('No Capistrano stages could be found.')
      return

    # Locate the stages.
    stage_commands = []
    stages = []
    for stage_file in os.listdir(stages_folder):
      stage_commands.append(stage_file.replace('.rb', ''))
      stages.append(stage_file.replace('.rb', '').title())

    # Define callback to run Capistrano when stage is selected.
    def stage_deploy(i):

      # If i = -1, they hit escape or didn't make a selection
      if i == -1:
        return

      # Construct the command.
      cmd = self.command.command_string(stage_commands[i] + ' deploy')

      # Run the selected deployment.
      self.window.run_command('exec', {
        'cmd': [cmd],
        'shell': True,
        'working_dir': project_folder,
        'syntax': 'Packages/ShellScript/Shell-Unix-Generic.tmLanguage'
      })

    self.window.show_quick_panel(stages, stage_deploy)

class CapistranoRailsRunTaskCommand(CapistranoRailsCommand):

  def run(self):

    # Init configuration.
    self.load_config()

    # Locate the project folder.
    project_folder = self.window.folders()[0]

    # Ensure the open folder is a Rails project with Capistrano.
    stages_folder = project_folder + '/' + self.stages_folder
    if not os.path.isdir(stages_folder):
      sublime.message_dialog('No Capistrano stages could be found.')
      return

    # Locate the stages.
    stage_commands = []
    stages = []
    for stage_file in os.listdir(stages_folder):
      stage_commands.append(stage_file.replace('.rb', ''))
      stages.append(stage_file.replace('.rb', '').title())

    # Define callback to run task when selected.
    def select_task(i):

      # If i = -1, they hit escape or didn't make a selection
      if i == -1:
        return

      # Construct the command.
      task = self.tasks[i]
      if type(task) is list:
        task = task[0]
      cmd = self.command.command_string(self.stage + ' ' + task)

      # Run the selected task.
      self.window.run_command('exec', {
        'cmd': [cmd],
        'shell': True,
        'working_dir': project_folder,
        'syntax': 'Packages/ShellScript/Shell-Unix-Generic.tmLanguage'
      })

    # Define callback to run Capistrano when stage is selected.
    def select_stage(i):
      # If i = -1, they hit escape or didn't make a selection
      if i == -1:
        return

      # Store selected stage.
      self.stage = stage_commands[i]

      # Parse each task into a string or string array.
      tasks = []
      for line in self.command.run_output(stage_commands[i] + ' -T').splitlines():
        line = line.split()
        cmd = line[1]

        if len(line) >= 2 and line[2] == '#':
          # Description is included.
          desc = ' '.join(line[3:])
          tasks.append([cmd, desc])
        else:
          # No description.
          tasks.append(cmd)

      # Store tasks for later reference.
      self.tasks = tasks

      self.window.show_quick_panel(tasks, select_task)

    self.window.show_quick_panel(stages, select_stage)