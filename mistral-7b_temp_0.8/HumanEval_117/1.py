
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
    while i < len(s):
        count = 0
        temp = ""
        while i < len(s) and s[i].isalpha():
            if s[i] not in 'aeiouAEIOU':
                count += 1
                temp += s[i]
            else:
                break
            i += 1
        if count == n:
            res.append(temp)
    return res

