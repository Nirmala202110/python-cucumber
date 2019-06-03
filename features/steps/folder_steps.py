from behave import *
from nose.tools import assert_equal, assert_true


@step('user navigates to the settings page')
def step_impl(context):
    context.settings_page.navigate_to_settings()


@when('user adds a folder with name "{name}"')
def step_impl(context, name):
    context.settings_page.create_folder(name)


@then('a folder is successfully created')
def step_impl(context):
    context.settings_page.delete_folder()



