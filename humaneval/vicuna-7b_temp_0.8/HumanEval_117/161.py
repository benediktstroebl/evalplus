
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
    result = []
    i = 0
    while i < len(s):
        if s[i] == " " and i < len(s)-1 and s[i+1] == " ":
            i += 2
            continue
        elif (s[i] == "b" or s[i] == "d" or s[i] == "f" or s[i] == "h" or s[i] == "j" or s[i] == "k" or s[i] == "m" or s[i] == "n" or s[i] == "p" or s[i] == "r" or s[i] == "s" or s[i] == "t" or s[i] == "w" or s[i] == "z" or s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" or s[i] == "v" or s[i] == "y") and (i < len(s)-1 and s[i+1] == " " or i == len(s)-1):
            i += 1
        else:
            result.append(s[i])
            i += 1
    return result
