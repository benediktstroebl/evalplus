
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
    s = s.strip()
    words = []
    if s == '':
        return words
   
    word_start = 0
    word_end = 0
    while word_end < len(s):
        if s[word_end].isalpha():
            # increase word_end by 1 if we hit a letter
            word_end += 1
            continue
        char = s[word_start:word_end]
        if is_consonant(char, n):
            words.append(char)
            word_end += 1
            continue
        if is_consonant(s[word_end], n):
            words.append(s[word_start:word_end])
            word_end += 1
            continue
        else:
            word_end += 1
        word_start = word_end
    if word_end == len(s):
        words.append(s[word_start:word_end])
    return words
