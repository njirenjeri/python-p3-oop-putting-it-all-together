#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = page_count
        # self._turn_page = turn_page
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    # @property
    # def turn_page(self):
    #     return self._turn_page
    
    # @turn_page.setter
    # def turn_page(self, turn_page):
    #     # if isinstance(turn_page, str):
    #     self._turn_page = turn_page
    #     print("Flipping the page...wow, you read fast!")
    
    
        