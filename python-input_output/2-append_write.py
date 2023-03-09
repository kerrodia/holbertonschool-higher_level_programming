#!/usr/bin/python3
"""
This module contains function that appends
a string at the end of a text file and
returns number of characters added
"""


def append_write(filename="", text=""):
    """
     function that appends a string at the end of a text file (UTF8)
     and returns the number of characters added:
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return (myFile.write(str(text)))
