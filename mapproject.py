
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
       dictTags = {}
       for event, elem in ET.iterparse(filename):
           if elem.tag in dictTags:
               dictTags[elem.tag] +=1
           else:
               dictTags[elem.tag] = 1
       return dictTags

def get_user(element):
    return


def process_map(filename):
    users = {}
    for _, element in ET.iterparse(filename, events =('start',)):
            if 'uid' in element.attrib:
              if element.attrib['uid'] in users:
                users[element.attrib['uid']] += 1
              else:
                users[element.attrib['uid']] = 1

    return users

def test():

   tags = count_tags('Udacity/johannesburg_south-africa.osm')
   pprint.pprint(tags)
   users = process_map('Udacity/johannesburg_south-africa.osm')
   pprint.pprint(users)

   

if __name__ == "__main__":
   test()