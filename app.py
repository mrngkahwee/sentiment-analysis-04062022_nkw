#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from textblob import TextBlob
#Flask or Jango --> Flask is easier to use
#React (front end) + Flask (back end)


# In[ ]:


from flask import Flask


# In[ ]:


from flask import render_template,request
#render throw the template
#request is a flask terminology, but in web protocol: GET


# In[ ]:


app = Flask(__name__)
#Whole flash object into a variable
#1970 when we first started programming language
#need to compile to Machine code
#cloud env, to confirm that it is your own program and not others


# In[ ]:


@app.route("/", methods = ["GET","POST"])   #got S

#declarator - before run some function, do some action
#put this route objection function
#embed into a function

def index():   #first function, html first to call is also index
    if request.method == "POST":   #no S
        text = request.form.get("text") #gives output below if you typed in browser
        print(text)
        r= TextBlob(text).sentiment
        return(render_template("index.html",result =r))
    else:
        return(render_template("index.html", result="waiting...")) #flask style
        
    


# In[ ]:


if __name__ == "__main__":   #run your own program not others!
    app.run()   
#protect cloud from running illegal software
#port 5000 default from Flask
#if 5000 cannot work
#app.run(host='0.0.0.0',port=80)   #127.0.0.1


# In[ ]:




