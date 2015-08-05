#!/usr/bin/python2.7

import cgi
import json
import subprocess

jarpath = '/var/www/direwolf/javaApi/tagParser.jar'

def main():
    form = cgi.FieldStorage()
    text = form.getvalue('text', '')
    results = subprocess.check_output(['java', '-jar', jarpath, text])
    print 'Content-Type: text/plain\r\n'
    print results

if __name__ == '__main__':
    main()

