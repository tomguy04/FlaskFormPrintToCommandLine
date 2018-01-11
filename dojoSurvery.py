# Assignment: Dojo Survey
# Build a flask application that accepts a form submission, redirects, and presents the submitted data 
# on a results page.

# The goal is to help you get familiar with sending POST requests through a form 
# and displaying that information. 


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
def data():
   print "Got Post Info"
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   print "*" * 80, name
   print "*", location
   print "*", language
   print "*", comment
   return render_template("data.html", myname = name, mylocation = location, mylanguage = language, mycomment = comment)
   
app.run(debug=True) # run our server


# Just for reference, here is the form html
# <form action='/process' method='post'>
#     <p>Your Name:<input type='text' name='name'></p>
#     <p>Dojo Location:<input type='text' name='location'></p>
#     <p>Favorite Language:<input type='text' name='language'></p>
#     <p>Comment:<input type='text' name='comment'></p>
