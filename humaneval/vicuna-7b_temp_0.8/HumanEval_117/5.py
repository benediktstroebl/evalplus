
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
    # Avoid using any global variables
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]

    words = s.split()
    cons = []
    for word in words:
        con = 0
        for letter in word:
            if chr(ord("b") + 1) == letter:
                con += 1
            elif chr(ord("p") + 1) == letter:
                con += 2
            elif chr(ord("s") + 1) == letter:
                con += 1
            elif chr(ord("z") + 1) == letter:
                con += 2
            elif chr(ord("n") + 1) == letter:
                con += 1
        if con == n:
            cons.append(word)
    return cons
