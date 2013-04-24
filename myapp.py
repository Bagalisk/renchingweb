#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib2
import os
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
    def get(self):
        r = self.response
        template_values = { }

        request = urllib2.unquote(self.request.path)

        if request=='/':
            path = os.path.join(os.path.dirname(__file__), 'index.html')
        else:
            path = os.path.join(os.path.dirname(__file__), request+'.html')

        r.out.write(template.render(path, template_values))
        
class CommandHandler(webapp2.RequestHandler):
    def get(self):
        r = self.response
        command = urllib2.unquote(self.request.path)
        r.write(command)
        
        if command == '/info':
            r.write('ssss')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    , ('/.*', CommandHandler)
], debug=True)
