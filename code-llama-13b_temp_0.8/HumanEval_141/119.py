
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """

    #1
    #Python’s Regular Expression library provides powerful tools to work with regular expressions.
    #It is accessible through the standard library’s re module.

    import re

    #2
    #You can either use a string to represent the pattern, or use one of the constants provided by 
    #the re module for common patterns.
    #Examples:
    #"cat"	    #A literal “cat”
    #"\\d"	    #Any digit, i.e. [0-9]
    #"\\D"	    #Any non-digit, i.e. [^0-9]
    #"\\s"	    #Any whitespace character, i.e. [ \t\n\r\f\v]
    #"\\S"	    #Any non-whitespace character, i.e. [^ \t\n\r\f\v]
    #"\\w"	    #Any alphanumeric character (a-zA-Z0-9_), i.e. [a-zA-Z0-9_]
    #"\\W"	    #Any non-alphanumeric character (i.e. not one of a-zA-Z0-9_), i.e. [^a-zA-Z0-9_]

    #3
    #The pattern can also be compiled using the re.compile() function.
    #Examples:
    #re.compile("ab")	        #A compiled pattern object.
    #re.compile(r"\d")	    #A compiled pattern object.
    #re.compile("\\d")	    #A compiled pattern object.

    #4
    #The re.match() function checks whether a string matches a pattern (the string at the very beginning).
    #The re.search() function checks whether a string contains a pattern (the string anywhere).
    #The re.findall() function returns a list of all substrings that match a pattern.
    #The re.finditer() function returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern.

    #5
    #This function returns a Match object if it was successful, and returns None
