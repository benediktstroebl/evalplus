
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
    # split string into words
    words = s.split()
    # check if empty
    if not words:
        return []
    # initialize result list
    result = []
    # iterate through words
    for word in words:
        # initialize count to 0
        count = 0
        # iterate through the word
        for letter in word:
            if letter.is_consonant():
                count += 1
        # check if count is equal to n
        if count == n:
            # add word to result list
            result.append(word)
    return result