from flask import Flask , render_template

import time

app = Flask(__name__ ,static_url_path='/static')


def getTime():
  the_time = time.localtime()
  return time.strftime(' %I:%M:%S %p',the_time)


@app.route('/')
def index():
  context = {'server_time':getTime()}
  return render_template('index.html',context=context)
  








if __name__ == "__main__":
  app.run(debug=True)
