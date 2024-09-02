
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

    # Input: String s and an integer n.
    # Output: A list of words from string s that have exactly n consonants.
    # Examples:
    # select_words("Mary had a little lamb", 4) ==> ["little"]
    # select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    # select_words("simple white space", 2) ==> []
    # select_words("Hello world", 4) ==> ["world"]
    # select_words("Uncle sam", 3) ==> ["Uncle"]

    # a = string
    # n = number of consonants

    # 1. Split s into words:
    #    b = list of strings
    b = s.split()
    # print(b)

    # 2. Filter to keep only the words with n consonants:
    #    c = list of strings
    c = [word for word in b if len(find_consonants(word)) == n]
    # print(c)

    return c

