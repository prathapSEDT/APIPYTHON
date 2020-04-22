from configparser import ConfigParser
import pytest
import allure

class Utils():

    @pytest.fixture(scope='session')
    def pre_and_post_activities(self):
        self.load_ConfigFile()
        yield

    @allure.step("Loading Config file")
    def load_ConfigFile(self):
        global config
        config=ConfigParser()
        config.read("../Configuration/Environment.cnf")
    @allure.step("Get Data from the section : {0} for the field : {1} from the config file")
    def getConfigData(self,section,property):

        return config.get(section,property)







