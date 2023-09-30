from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('Launching Chrome Browser')
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print('Launching Firefox Browser')
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):                    # This will get the value from CLI Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                            # This will return the Browser value to setup function
    return request.config.getoption("--browser")


###################### PyTest HTML Reports ###################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Durga Prasad Devarakonda'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)