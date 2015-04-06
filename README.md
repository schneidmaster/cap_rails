# CapRails

A [Sublime Text](http://www.sublimetext.com/) plugin that executes [Capistrano](http://capistranorb.com/) deployments and tasks for Rails projects within the Sublime Text console.

## Installation

### Prerequisites

You must have Capistrano set up and configured for your project.

### Recommended:

Install CapRails via [Package Control](http://wbond.net/sublime_packages/package_control).

### Manual:

1. Navigate to the Sublime Text Packages folder (You can find the location of the Packages folder [here](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory)).

2. Run the git clone command right inside the packages directory: `git clone git@github.com:schneidmaster/cap_rails.git "CapRails"`

3. Restart Sublime Text.

## Usage

CapRails will run any deployment or Capistrano task configured in the active project. Activate the Command Palette (`⌘+shift+P` or `ctrl+shift+P`) and type `Capistrano: Deploy` or `Capistrano: Run Task`. You will be given the option to select the stage and/or task you'd like to run, and the deployment/task will then run within the Sublime Text console.

CapRails supports rvm and rbenv, in addition to the system ruby installation. The desired ruby, ruby installation path, and path to deployment configuration can all be set in the settings.

## System Support

CapRails should hypothetically work on all operating systems and ruby installations. However, it's only been seriously tested on Mac OSX and RVM. If you find an problem, submit an issue or better yet a pull request.

## Contributing

1. Fork it ( https://github.com/schneidmaster/cap_rails/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## Credits

I heavily referenced the [Sublime Rubocop](https://github.com/pderichs/sublime_rubocop/) package by Patrich Derichs to determine how to execute commands.

