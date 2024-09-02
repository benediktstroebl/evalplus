
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

    import re
    consonants = [chr(x) for x in range(ord('a'), ord('z') + 1) if not x in [ord('a'), ord('e'), ord('i'), ord('o'), ord('u')]]
    consonants = ''.join(consonants)
    consonants = '[%s]' % consonants
    p = re.compile(consonants, re.UNICODE)
    words = [x for x in p.findall(s) if len(x) == n]
    return words
