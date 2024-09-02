
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
    from string import ascii_lowercase
    from collections import defaultdict
    res = []
    current_word = ""
    word_count = defaultdict(lambda:0)
    for c in s.lower():
        if c in ascii_lowercase:
            word_count[current_word] += 1
            if c in "bcdfghjklmnpqrstvwxyz":
                current_word += c
            else:
                current_word += " "
        else:
            current_word += " "
    for word, count in word_count.items():
        if count == n:
            res.append(word.strip())
    return res

