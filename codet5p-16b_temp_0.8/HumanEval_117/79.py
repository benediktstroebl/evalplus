
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

    def is_valid_word(s, n):
        return len(s) == n and n > 0

    def is_valid_string(s):
        return s and s.strip()

    if not is_valid_string(s):
        return []
    s = s.lower()
    s = s.split()
    words = []
    for word in s:
        if is_valid_word(word, n):
            words.append(word)
    return words
