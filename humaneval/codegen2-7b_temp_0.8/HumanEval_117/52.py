
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
    """
    while len(s) > 0:
        if s[0] == " ":
            s = s[1:]
        else:
            if len(s) == n:
                if s[0] in vowels:
                    res.append(s[0])
                s = s[1:]
            else:
                s = s[1:]
    return res
    """
    return [x for x in s if x in vowels and len(x)==n]
