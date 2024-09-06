
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
    assert type(s) == str, "Argument should be a string"
    assert type(n) == int, "Argument should be an integer"
    assert 0 <= n <= 10000, "Argument should be between 0 and 10000"
    words = s.split(" ")
    r = []
    for word in words:
        if len([char for char in word if char.isalpha() and char.islower()]) == n:
            r.append(word)
    return r
