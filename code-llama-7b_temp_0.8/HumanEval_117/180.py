
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
    word_list = []
    for word in s.split():
        if len(word) == n and word.count('a') == 0 and word.count('e') == 0 and word.count('i') == 0 and word.count('o') == 0 and word.count('u') == 0 and word.count('A') == 0 and word.count('E') == 0 and word.count('I') == 0 and word.count('O') == 0 and word.count('U') == 0:
            word_list.append(word)
    return word_list
