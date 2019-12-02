import requests
import json
from math import*
from collections import OrderedDict


def main():

    print("Welcome to the Matt Maps!")
    print("I'll be your personal guide today.")
    print("")
    tripNum = int(input("How many destinations are on the road for today?\n"))
    print("\nAWESOME!")

    i = 0
    locationList = []
    while i <= tripNum:
        print("")
        if i == 0:
            location = input("Where are you starting out from? (Please exclude zip code and any suite/apt #'s "
                             "from all addresses)\n")

        else:
            location = input("What is destination #" + str((i)) + "?\n")

        locationList.append(location)
        i+=1

    print("\nGreat.")
    outputList = []
    j = 0

    print("\nHow many of the following details would you like to see about your trip?\n")
    displayOptions();
    outputNum = int(input())
    print("")
    if outputNum == 5:
        for x in range(5):
            outputList.append(x + 1)
    else:
        while j < outputNum:
            output = int(input("What is detail #" + str(j + 1) + "?\n"))
            outputList.append(output)
            j += 1

    tripNum+= 1
    k = 0

    print("\nAlright, here are the details for your trip!")
    while k < outputNum:

        if outputList[k] == 1:
            tripSteps(tripNum, locationList)

        if outputList[k] == 2:
            tripDistance(tripNum, locationList)

        if outputList[k] == 3:
            tripTime(tripNum, locationList)

        if outputList[k] == 4:
            tripLatLong(tripNum, locationList)

        if outputList[k] == 5:
            tripElevation(tripNum, locationList)

        k+=1

    print("\nOkay! You're all set to get on the road. This will be such fun!")


def tripSteps(tripNum, locationList):
    print("")
    print("DIRECTIONS\n")

    i = 0
    while i < (tripNum-1):
        trip1 = Steps(locationList[i], locationList[i+1])
        print(trip1.calculateSteps(locationList[i], locationList[i+1]))
        if (i+2) < tripNum:
            print("\nTo continue to " + locationList[i+2] + ":")

        i+=1

def tripDistance(tripNum, locationList):
    print("")

    e = 0
    totalDistance = 0
    while e < (tripNum-1):
        dist1 = Distance(locationList[e], locationList[e+1])
        distance = (dist1.calculateDistance(locationList[e], locationList[e+1]))
        totalDistance += distance
        e+=1

    print("TOTAL DISTANCE: " + str(round(totalDistance)) + " miles")

def tripTime(tripNum, locationList):
    print("")


    totalTime = 0
    u = 0
    while u < (tripNum-1):
        time1 = Time(locationList[u], locationList[u+1])
        time = (time1.calculateTime(locationList[u], locationList[u+1]))
        totalTime += time
        u+=1

    print("TOTAL TIME: " + str(round(totalTime)) + " minutes")


def tripLatLong(tripNum, locationList):
    print("")
    print("LATLONGS")

    a = 0
    while a <(tripNum-1):

        latLong = LatLong(locationList[a], locationList[a+1])
        lat, longi, lat2, longi2 = (latLong.calculateLatLong(locationList[a], locationList[a+1]))


        if lat < 0:
            lat = str(abs(lat)) + "S"

        else:
            lat = str(lat) + "N"

        if longi < 0:
            longi = str(abs(longi)) + "W"

        else:
            longi = str(longi) + "E"

        if lat2 < 0:
            lat2 = str(abs(lat2)) + "S"

        else:
            lat2 = str(lat2) + "N"

        if longi2 < 0:
            longi2 = str(abs(longi2)) + "W"

        else:
            longi2 = str(longi2) + "E"

        if a == 0:

            print(lat, longi)
            print(lat2, longi2)


        else:
            print(lat2, longi2)

        a+=1

def tripElevation(tripNum, locationList):
    print("")
    print("ELEVATIONS")

    b = 0
    while b <(tripNum-1):

        elevation = Elevation(locationList[b], locationList[b+1])
        height, height2 = (Elevation.calculateElevation(locationList[b], locationList[b], locationList[b+1]))

        if b == 0:
            print(str(height) + " feet")
            print(str(height2) + " feet")
        else:
            print(str(height2) + " feet")

        b+=1

def displayOptions():
    print("1. Steps \n" +
          "2. Total Distance\n" +
          "3. Total Time\n" +
          "4. Latitude/Longitude\n" +
          "5. Elevation")


class Steps:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def set_start(self, start):
        self.__start = start
    def set_end(self, end):
        self.__end = end
    def get_start(self):
        return self.__end
    def get_location(self):
        return self.__end

    def calculateSteps(self, start, end):
        link = "http://open.mapquestapi.com/directions/v2/route?key=GPYZO7JeQjnmv5Rkt0nrOjmokh3Y4Cjk&from=" + start + \
               "%2CCA\&to=" + end

        f = requests.get(link)
        api = f.json()
        route = api['route']
        boundingBox = route['boundingBox']

        legs = route['legs']
        legsList = legs[0]
        maneuvers = legsList["maneuvers"]

        size = len(maneuvers)

        i = 0

        narrativeList = []
        while i < size:
            step = maneuvers[i]
            narrative = step["narrative"]
            print(narrative)
            i+=1

        return ""


class Distance:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def set_start(self, start):
        self.__start = start
    def set_end(self, end):
        self.__end = end
    def get_start(self):
        return self.__end
    def get_location(self):
        return self.__end

    def calculateDistance(self, start, end):
        link = "http://open.mapquestapi.com/directions/v2/route?key=GPYZO7JeQjnmv5Rkt0nrOjmokh3Y4Cjk&from=" + start\
               + "%2CCA\&to=" + end

        f = requests.get(link)
        api = f.json()
        route = api['route']

        distance = route['distance']

        return float(distance)


class Time:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def set_start(self, start):
        self.__start = start
    def set_end(self, end):
        self.__end = end
    def get_start(self):
        return self.__end
    def get_location(self):
        return self.__end


    def calculateTime(self, start, end):
        link = "http://open.mapquestapi.com/directions/v2/route?key=GPYZO7JeQjnmv5Rkt0nrOjmokh3Y4Cjk&from=" + start \
               + "%2CCA\&to=" + end

        f = requests.get(link)
        api = f.json()
        route = api['route']

        time = route["formattedTime"]
        hour, minute, sec = time.split(':')
        hour = int(hour)
        hour*=60

        sec = int(sec)
        sec/=60

        minute = int(minute)
        time = hour + minute + sec
        return time


class LatLong:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def set_start(self, start):
        self.__start = start
    def set_end(self, end):
        self.__end = end
    def get_start(self):
        return self.__end
    def get_location(self):
        return self.__end

    def calculateLatLong(self, start, end):
        link = "http://open.mapquestapi.com/directions/v2/route?key=GPYZO7JeQjnmv5Rkt0nrOjmokh3Y4Cjk&from=" + start \
               + "%2CCA\&to=" + end

        f = requests.get(link)
        api = f.json()
        route = api['route']
        boundingBox = route['boundingBox']
        lr = boundingBox['lr']

        lng = lr['lng']
        lat = lr['lat']

        ul = boundingBox['ul']
        lng2 = ul['lng']
        lat2 = ul['lat']

        longitude = float(lng)
        latitude = float(lat)
        longitude2 = float(lng2)
        latitude2 = float(lat2)

        if longitude < 0:
            longitude = round(longitude, 2)
            longFinal = longitude

        else:
           longitude = round(longitude, 2)
           longFInal = longitude

        if latitude < 0:
            latitude = round(latitude, 2)
            latFinal = latitude

        else:
           latitude = round(latitude, 2)
           latFinal = latitude

        if longitude2 < 0:
            longFinal2 = longitude2

        else:
           longFinal2 = longitude2

        if latitude2 < 0:
            latitude2 = round(latitude2, 2)
            latFinal2 = latitude2

        else:
           latitude2 = round(latitude2, 2)
           latFinal2 = latitude2


        return latFinal, longFinal, latFinal2, longFinal2


class Elevation:
    def __init__(self, start, end):


        self.__start = start
        self.__end = end

        def set_start(self, start):
            self.__start = start
        def set_end(self, end):
            self.__end = end
        def get_start(self):
            return self.__end
        def get_location(self):
            return self.__end

    def calculateElevation(self, start, end):
        link = "http://open.mapquestapi.com/directions/v2/route?key=GPYZO7JeQjnmv5Rkt0nrOjmokh3Y4Cjk&from=" + start \
               + "%2CCA\&to=" + end

        f = requests.get(link)
        api = f.json()
        route = api['route']
        boundingBox = route['boundingBox']
        lr = boundingBox['lr']

        lng = lr['lng']
        lat = lr['lat']

        ul = boundingBox['ul']
        lng2 = ul['lng']
        lat2 = ul['lat']

        longitude = float(lng)
        latitude = float(lat)
        longitude2 = float(lng2)
        latitude2 = float(lat2)
        if longitude < 0:
            longFinal = longitude

        else:
           longFInal = longitude

        if latitude < 0:
            latFinal = latitude

        else:
           latFinal = latitude

        if longitude2 < 0:
            longFinal2 = longitude2

        else:
           longFinal2 = longitude2

        if latitude2 < 0:
            latFinal2 = latitude2

        else:
           latFinal2 = latitude2

        elLink = "http://open.mapquestapi.com/elevation/v1/profile?key=GPYZO7JeQjnmv5Rkt0nrOjmokh3Y4Cjk&shapeFormat" \
                 "=raw&latLngCollection=" + str(latFinal) + "," + str(longFinal)
        g = requests.get(elLink)
        apiEL = g.json()
        elevation = apiEL['elevationProfile']
        elevationList = elevation[0]
        height = elevationList['height']

        elLink2 = "http://open.mapquestapi.com/elevation/v1/profile?key=GPYZO7JeQjnmv5Rkt0nrOjmokh3Y4Cjk&shapeFormat" \
                  "=raw&latLngCollection=" + str(latFinal2) + "," + str(longFinal2)
        h = requests.get(elLink2)
        apiEL2 = h.json()
        elevation2 = apiEL2['elevationProfile']
        elevationList2 = elevation2[0]
        height2 = elevationList2['height']

        return height, height2


main()

