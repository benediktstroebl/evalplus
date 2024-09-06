
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
    if s == "":
        return []
    n = n % 26
    chars = list(s)
    words = []
    current_word = ""
    for i in range(len(chars)):
        if chars[i] in "aeiou":
            continue
        else:
            current_word += chars[i]
            if chars[i + 1] in "aeiou":
                words.append(current_word)
                current_word = ""
    return words

