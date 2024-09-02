
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
    # sort by length of words
    s = s.split(" ")
    l = []
    for i in s:
        l.append((i, len(i)))
    l.sort(key=lambda tup: tup[1], reverse=True)
    # print(l)
    s = [x[0] for x in l]
    # print(s)
    # print("".join(s))
    # return s

    l = []
    for i in range(len(s)):
        if s[i].lower().count("a") + s[i].lower().count("e") + s[i].lower().count("i") + s[i].lower().count("o") + s[i].lower().count("u") == n:
            l.append(s[i])
    return l
