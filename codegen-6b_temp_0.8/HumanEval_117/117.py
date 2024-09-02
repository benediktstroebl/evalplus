
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
    candidate_words = []

    if len(s) == 0:
        return candidate_words

    for i in range(0, len(s)):
        word = s[i:]

        # sanity check
        if not word or not isinstance(word, str):
            break

        # current word has the number of letters we want
        if len(word) == n:
            candidate_words.append(word)

        # current word is too short
        if len(word) < n:
            break

        # try a new word
        num_vowels = 0
        for letter in word:
            if letter not in VOWELS:
                num_vowels += 1

        if num_vowels == n:
            candidate_words.append(word)

    return candidate_words
