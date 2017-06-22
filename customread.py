from fileparser import Fileparser
from collections import defaultdict
import time

# Function to find key with most unique values and to compute average
def simpleComputation(uniqueDict,type=0):
    max_key=""
    max_val=0
    if type == 1:
        avgDuration = defaultdict(list)
        for k, v in uniqueDict.items():
            avgDuration[k] = (1.0 * sum(v)) / len(v)
        return avgDuration
    else:
        for k,v in uniqueDict.items():
            if len(v) > max_val:
                max_key = k
                max_val = len(v)
        return max_key

# Main Driver Function
def main():

    logFile1 = Fileparser("log_201612_01.csv")
    logFile2 = Fileparser("log_201612_02.csv")
    logFile1Lst=logFile1.readAllLines()
    logFile2Lst=logFile2.readAllLines()
    logFile1Lst.extend(logFile2Lst[1:])

    uniqueNetizens=defaultdict(set)
    avgTimeSpent=defaultdict(list)
    popularDate =defaultdict(set)
    popularSection=defaultdict(set)

    for eachitem in logFile1Lst[1:]:

        eachitem = eachitem.split(",")
        date=eachitem[0]
        userId=eachitem[1]
        country=eachitem[2]
        webAddress=eachitem[3]
        duration=eachitem[-1]

        if 'www.' in webAddress:
            section = webAddress.split("/")[1]
            if userId != '':
                popularSection[section].add(userId)
            avgTimeSpent[webAddress].append(int(duration) if duration !='' else 0)

        if country != '' and userId != '' and country != "unknown":
            uniqueNetizens[country].add(userId)
        try:
            time.strptime(date, '%m/%d/%y')
            if userId != '':
                 popularDate[date].add(userId)
        except ValueError:
            continue

    maxCountry = simpleComputation(uniqueNetizens)
    print("a. From which country did the site receive the most unique visitors?")
    print(maxCountry)
    avgDuration = simpleComputation(avgTimeSpent,1)
    print("b. What was the average time spent visiting a page?")
    print(avgDuration)
    popularDay = simpleComputation(popularDate)
    print("c. What was the most popular day to visit the site (as calculated by the number of unique visitors)? What day of the week was that date? ")
    print (time.strftime("%A", time.strptime(popularDay, '%m/%d/%y')))
    popular_section = simpleComputation(popularSection)
    print("d. What is the most popular section of the webiste (as calculated by the number of unique visitors)?")
    print(popular_section)

if __name__ == '__main__':
    main()