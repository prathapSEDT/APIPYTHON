from configparser import ConfigParser
import pytest
import allure
import os

class Utils():

    @pytest.fixture(scope='session')
    def pre_and_post_activities(self):

        self.load_ConfigFile()
        yield

    @allure.step("Loading Config file")
    def load_ConfigFile(self):
        print(os.getcwd())
        global config
        config=ConfigParser()
        config.read("../Environment.cnf")
        print("**********Reading config file***************")
    @allure.step("Get Data from the section : {0} for the field : {1} from the config file")
    def getConfigData(self,section,property):
        print("*****************************************************")
        return config.get(section,property)







