
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
    res = []
    i = 0
    # TODO: Fill in the function
    while i < len(s):
        words = []
        words.append(s[i:i+n])
        count = 0
        for char in words[0]:
            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                pass
            else:
                count += 1
        if count == n:
            res.append(words[0])
        i += 1
    return res


