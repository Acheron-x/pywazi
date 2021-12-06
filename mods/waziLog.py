import time
from mods.waziColor import waziColor

class waziLog:
    # A class for log printing and exporting.
    # 用于日志打印和导出的一个类。
    def __init__(self):
        super(waziLog, self).__init__()
        self.color = waziColor()
        self.min = -1
        self.save = False
        self.saveName = ""
        self.setSaveName()

    def setSaveName(self):
        self.saveName = "LOG_" + time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(time.time())) + ".log"

    def needSave(self, boolean):
        self.save = boolean
        return self.save

    def setMinDisplayLevel(self, levelNumber):
        self.min = levelNumber
        return self.min

    def outputLog(self, text):
        if self.save:
            with open(self.saveName, "a", encoding = "utf-8") as f:
                f.write(text + "\n")

    def log(self, level, text):
        if level == "debug":
            printText = "[DEBUG \t" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "] " + text
            if self.min >= 3:
                color = self.color.RGBToHex(0xff, 0xe9, 0x00)
                self.color.print({
                    "color": color,
                    "text": printText
                })
            waziLog.outputLog(self, printText)
        if level == "info":
            printText = "[INFO \t" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "] " + text
            if self.min >= 2:
                color = self.color.RGBToHex(0x00, 0xaa, 0xda)
                self.color.print({
                    "color": color,
                    "text": printText
                })
            waziLog.outputLog(self, printText)
        if level == "warn":
            printText = "[WARN \t" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "] " + text
            if self.min >= 1:
                color = self.color.RGBToHex(0xff, 0xaa, 0x4d)
                self.color.print({
                    "color": color,
                    "text": printText
                })
            waziLog.outputLog(self, printText)
        if level == "error":
            printText = "[ERROR \t" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "] " + text
            if self.min >= 0:
                color = self.color.RGBToHex(0xff, 0x72, 0x76)
                self.color.print({
                    "color": color,
                    "text": printText
                })
            waziLog.outputLog(self, printText)