
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
    # case where the string is empty
    if s == "":
        return []

    # split the string into individual words
    words = s.split(" ")

    result = []
    # count the number of consonants in each word
    for word in words:
        count = 0
        for c in word:
            if c in "bcdfghjklmnpqrstvwxz":
                count += 1
            if count == n:
                result.append(word)
    return result

