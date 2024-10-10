#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=0):
        self.page_count = page_count
        self.title = title 
        self.total_pages = 0
        self.title_types = []
        
    @property 
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not (type(value)==int):
            print("page_count must be an integer")
        else: 
            self._page_count = value 

    def turn_page(self): 
            print("Flipping the page...wow, you read fast!")
       
    