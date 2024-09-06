
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # replace underscore with your name
    _ = "YOUR NAME"
    # code goes here
    # (1)
    # create a list that stores the index of each space in the string
    # for example, if the string s is 'Mary had a little lamb',
    # then the list will be [3, 10]
    # note: in python, the string 'Mary had a little lamb' is
    # represented as an immutable tuple
    # for example, type(s) would return str
    #                                  return tuple
    # so, in order to change the elements in the tuple, you need to
    # create a list that stores the index of each space in the string

    # (2)
    # return an empty list if the string is empty

    # (3)
    # create a list that stores all words from the string
    # each element in the list stores the index of the word in the string
    # for example, if the string s is 'Mary had a little lamb',
    # then the list will be [0, 3,
