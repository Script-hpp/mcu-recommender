## Data is providen from https://github.com/AugustoMarcelo/mcuapi
import requests
import time


class Marvel:
    def __init__(self,arg1, arg2, arg3, arg4, arg5):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5

    

    movie_list = []
    movie_cover = []
    movie_trailer = []
    movie_release_date = []
    movie_description = []

    series_list = []
    series_cover = []
    series_trailer = []
    series_release_date = []
    series_description = []


    def getResponse(self):
        r = requests.get("https://mcuapi.herokuapp.com/api/v1/movies").json()
        return r["data"]
    
    def getSeries(self):
        r = requests.get("https://mcuapi.herokuapp.com/api/v1/tvshows").json()
        return r["data"]
    
    def pushToList(self, lst, val):
        return lst.append(val)


    def getIndexRange(self):
        return len(self.getResponse())
    
    def getSeriesRange(self):
        return len(self.getSeries())


    
    def getDatas(self):
        startTime = time.time()
        response = self.getResponse()
        for i in range(self.getIndexRange()):
            self.pushToList(self.movie_list, response[i][self.arg1]) # push movie names to list
            self.pushToList(self.movie_cover, response[i][self.arg2]) # push movies cover urls to list
            self.pushToList(self.movie_trailer, response[i][self.arg3]) # push movies overviews to list
            self.pushToList(self.movie_release_date, response[i][self.arg4]) # push movies release dates to list
            self.pushToList(self.movie_description, response[i][self.arg5]) # push movies release dates to list

        endTime = time.time()
        howMuchTime = endTime - startTime
        print(str(howMuchTime) + " sec")
    
    def getSeriesData(self):
        startTime = time.time()
        response = self.getSeries()
        for i in range(self.getSeriesRange()):
            self.pushToList(self.series_list, response[i][self.arg1]) # push series names to list
            self.pushToList(self.series_cover, response[i][self.arg2]) # push seriess cover urls to list
            self.pushToList(self.series_trailer, response[i][self.arg3]) # push seriess overviews to list
            self.pushToList(self.series_release_date, response[i][self.arg4]) # push seriess release dates to list
            self.pushToList(self.series_description, response[i][self.arg5]) # push seriess release dates to list

        endTime = time.time()
        howMuchTime = endTime - startTime
        print(str(howMuchTime) + " sec")
    

            


            

    




    def test_func(self):
        # print(self.getResponse())
        self.getDatas()
        print(self.getSeriesRange())

        
        return None

