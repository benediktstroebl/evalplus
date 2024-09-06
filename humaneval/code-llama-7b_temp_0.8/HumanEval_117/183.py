
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
    #take string and split it into a list
    #make a new list
    #go through the list and append words with desired amount of consonants to new list
    words = s.split()
    final = []
    for i in words:
        if len(i) == n:
            if i.lower() == "a":
                pass
            elif i.lower() == "e":
                pass
            elif i.lower() == "i":
                pass
            elif i.lower() == "o":
                pass
            elif i.lower() == "u":
                pass
            else:
                final.append(i)
    return final

