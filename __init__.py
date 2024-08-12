from googletrans import Translator
from configparser import ConfigParser
from config import ConfigUtils
import logger,json,sys,os

translator = Translator()
config = ConfigParser()
configUtils = ConfigUtils()

if configUtils.checkConfigFile() == False:
    configUtils.initConfigFile(os.path.realpath(sys.argv[0]))