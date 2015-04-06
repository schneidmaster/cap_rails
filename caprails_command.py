import os, subprocess

RVM_DEFAULT_PATH = '~/.rvm/bin/rvm-auto-ruby'
RBENV_DEFAULT_PATH = '~/.rbenv/bin/rbenv'

class CapRailsCommand(object):
  def __init__(self, args):
    self.set_default_paths()
    vars(self).update(args)

  def set_default_paths(self):
    self.rvm_auto_ruby_path = RVM_DEFAULT_PATH
    self.rbenv_path = RBENV_DEFAULT_PATH

  def load_cmd_prefix(self):
    self.cmd_prefix = ''
    if not self.load_rvm():
      self.load_rbenv()

  def load_rvm(self):
    if self.use_rvm:
      rvm_cmd = os.path.expanduser(self.rvm_auto_ruby_path)
      self.cmd_prefix = rvm_cmd + ' -S'
      return True
    return False

  def load_rbenv(self):
    if self.use_rbenv:
      rbenv_cmd = os.path.expanduser(self.rbenv_path)
      self.cmd_prefix = rbenv_cmd + ' exec'
      return True
    return False

  def run_output(self, task):
    call_list = self.command_list(task)
    p = subprocess.Popen(call_list, stdout=subprocess.PIPE)
    bts = p.communicate()[0]
    return str(bts, 'utf-8')

  def command_list(self, task):
    result = []
    self.load_cmd_prefix()
    result += self.cmd_prefix.split()
    result += 'cap'.split()
    result += task.split()
    return result

  def command_string(self, task):
    list = self.command_list(task)
    return " ".join(list)