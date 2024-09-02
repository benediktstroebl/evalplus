
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
    if n == 0:
        return []
    if not s:
        return []

    # split the string into a list of words and remove spaces
    lst = s.split()
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == "":
            lst.pop(i)
    lst_of_words = []

    for word in lst:
        if len(word) == n:
            lst_of_words.append(word)
    return lst_of_words

