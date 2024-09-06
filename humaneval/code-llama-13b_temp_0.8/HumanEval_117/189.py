
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
    # replace space with a comma
    new_s = s.replace(" ", ",")
    # split the s by comma
    new_s = new_s.split(',')
    # keep only the words with the length of n
    new_s = [i for i in new_s if len(i) == n]
    # split the s by space
    new_s = [i.split() for i in new_s]
    # return the list of the n th word
    return [i[n] for i in new_s]

