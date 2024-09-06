
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
    word_count = 0
    new_list = []
    for c in s:
        if c.isalpha():
            if c not in ("a", "e", "i", "o", "u"):
                word_count += 1
    for i in range(len(s)):
        if s[i] == " ":
            if word_count == n:
                new_list.append(s[i-word_count:i])
                word_count = 0
    return new_list

