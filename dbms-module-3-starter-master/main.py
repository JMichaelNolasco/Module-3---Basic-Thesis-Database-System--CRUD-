import json
import os
import urllib
from google.appengine.ext import ndb
from google.appengine.api import users
import jinja2
import webapp2
import json



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)





class Thesis(ndb.Model):
    year= ndb.StringProperty()
    title = ndb.StringProperty(indexed=True)
    abstract = ndb.StringProperty(indexed=True)
    adviser = ndb.StringProperty(indexed=True)
    section= ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class ThesisHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render())
        

    def post(self):
    	thesis =Thesis()

    	thesis.year = self.request.get('year')
        thesis.title = self.request.get('title')
        thesis.abstract = self.request.get('abstract')
        thesis.adviser = self.request.get('adviser')
        thesis.section = self.request.get('section')
        thesis.put()
        self.redirect('/success')



class APINewHandler(webapp2.RequestHandler):
    
    def get(self):
        CpE_Thesis= Thesis.query().order(-Thesis.date).fetch()
        thesis_list=[]
        for thesis in CpE_Thesis:
            thesis_list.append ({
                'id': thesis.key.urlsafe(),
                'year' : thesis.year,
                'title': thesis.title,
                'abstract': thesis.abstract,
                'adviser': thesis.adviser,
                'section': thesis.section
              
            })
        response = {
            'result' :'OK' ,
            'data' : thesis_list 
        }
        self.response.headers['Content-type'] = 'app/json'
        self.response.out.write(json.dumps(response))

    def post(self):
        thesis = Thesis()

        thesis.year = self.request.get('year')
        thesis.title = self.request.get('title')
        thesis.abstract = self.request.get('abstract')
        thesis.adviser = self.request.get('adviser')
        thesis.section = self.request.get('section')
        thesis.put()

        response = {
            'result': 'OK',
            'data':{
                'id': thesis.key.urlsafe(),
                'year' : thesis.year,
                'title': thesis.title,
                'abstract': thesis.abstract,
                'adviser': thesis.adviser,
                'section': thesis.section

            }
        }
        self.response.out.write(json.dumps(response))


app = webapp2.WSGIApplication([

    ('/api/thesis', APINewHandler),
    ('/home', ThesisHandler),
    ('/', ThesisHandler)
    
], debug=True)


