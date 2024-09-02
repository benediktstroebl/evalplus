
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

    # find all words in the string that are the correct length
    words = s.split()
    words_length = []
    for word in words:
        if len(word) == n:
            words_length.append(word)

    # find all consonants in the words
    consonant_count = 0
    for word in words_length:
        for letter in word:
            if letter not in 'aeiouAEIOU':
                consonant_count += 1
        if consonant_count == n:
            words_list.append(word)
        consonant_count = 0

    # return the list of words that contains exactly n consonants
    return words_list
