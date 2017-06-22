class Fileparser():
    '''
        File Parser Implementation.
    '''
    def __init__(self,fileName):
             self.logFile = open(fileName)
             self.fileName = fileName
             self.delimiter = ','

    # Function to read line by line from log file
    def readLine(self):
         logFileLine = self.logFile.readline().strip()
         tmp = logFileLine
         while logFileLine == "" or tmp.replace(self.delimiter,'') == '':
             logFileLine=self.logFile.readline()
             if logFileLine == '':
                 break
             else:
                 logFileLine = logFileLine.strip()
                 tmp = logFileLine
         if logFileLine != "":
             return logFileLine
         else:
             return None

    # Function to read all lines of the log file
    def readAllLines(self, type=0):
        if type ==0:
            logFile = Fileparser(self.fileName)
            eachLine = logFile.readLine()
            allLines=[]
            while eachLine is not None:
                allLines.append(eachLine)
                eachLine = logFile.readLine()
            return allLines
        else:
            return open(self.fileName)



