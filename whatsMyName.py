# Assignment: What's My Name?
# Create a project that allows users to submit a form.

# "/": renders a landing page with a form.

# "/process": the route your form should submit to. 
# In your process function, 
# print the user's name and redirect to root.

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form

#1
@app.route('/')
def index():
  return render_template("form.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
# WE ARE WAITING FOR A POST REQUEST
@app.route('/process', methods=['POST'])
def get_name():
   print "Got Post Info"
   name = request.form['name']
   print "*" * 80, name
   #redirects back to the '/' route
   #return render_template("form.html", myname = name)
   return redirect('/')
   

app.run(debug=True) # run our server

# from flask import Flask, render_template, request, redirect
# app = Flask(__name__)
# @app.route('/users/<username>/<myid>')
# def show_user_profile(username,myid):
#     print "*" * 80, username
#     print "*" * 80, myid
#     return render_template("index.html", user = username, id1 = myid)
# app.run(debug=True)