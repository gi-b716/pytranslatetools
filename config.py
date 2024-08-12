from configparser import ConfigParser
import os

class ConfigUtils:
    def __init__(self):
        self.config = ConfigParser()
    
    def checkConfigFile(self) -> bool:
        return os.path.isfile(".\\pttconfig.ini")

    def initConfigFile(self, path : str) -> None:    
        file = open("pttconfig.ini","w")
        file.close()
        self.config.add_section("Path")
        self.config.set("Path", "LanguageFilePath", "{}language.json".format(path[:-11]))
        # 在发布中为path[:-7]
        with open('pttconfig.ini', 'w') as configfile:
            self.config.write(configfile)