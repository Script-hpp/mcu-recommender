from mcu import Marvel
from flask import Flask,render_template,request,make_response,redirect,url_for, session

import random

app = Flask(__name__)

marvel = Marvel('title', 'cover_url', 'trailer_url','release_date', 'overview')


movie = "asd"


@app.route('/')
def index():
    n = random.randint(0,1)
    if n == 1:
        return redirect(url_for('films'))
    else:
        return redirect(url_for('series')) ##changes


@app.route('/films')
def films():
   n = random.randint(0,37)
   marvel.getDatas()
   cover_urls = marvel.movie_cover[n]
   movie = marvel.movie_list[n]
   movie_date = marvel.movie_release_date[n]
   movie_trailer = marvel.movie_trailer[n]
   movie_description = marvel.movie_description[n]      
   return render_template('index.html', user_image=cover_urls,movie_name=movie,movie_date=movie_date,movie_trailer=movie_trailer,movie_description=movie_description)


@app.route('/series')
def series():
   n = random.randint(0,15)
   marvel.getSeriesData()
   cover_urls = marvel.series_cover[n]
   movie = marvel.series_list[n]
   movie_date = marvel.series_release_date[n]
   movie_trailer = marvel.series_trailer[n]
   movie_description = marvel.series_description[n]      
   return render_template('series.html', user_image=cover_urls,movie_name=movie,movie_date=movie_date,movie_trailer=movie_trailer,movie_description=movie_description)





if __name__ == '__main__':
    app.run(debug=True)


