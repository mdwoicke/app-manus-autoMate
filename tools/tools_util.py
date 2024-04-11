from tools.FindDesktopPath import FindDesktopPath
from tools.ListAllFile import ListAllFile
from tools.ListDesktopFiles import ListDesktopFiles
from tools.OpenApplication import OpenApplicationAction


class ToolsUtil:
    @staticmethod
    def get_tools():
        return [OpenApplicationAction(), FindDesktopPath(), ListAllFile(), ListDesktopFiles()]
