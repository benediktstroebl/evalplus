
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
    # PLAN
    # case: string is empty
        # return empty list
    # case: string has consonant count
        # return the word as a list item
    # case: string does not have consonant count
        # return empty list
    
    # init word_list
    word_list = []

    # if string is empty:
    #   return empty list
    if len(s) == 0:
        return word_list

    # split string into individual words
    words = s.split()

    # iterate through each word
    for word in words:
        # init counter
        counter = 0

        # init consonant list
        consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

        # init word_lower
        word_lower = word.lower()
        
        # iterate through each letter in word
        for letter in word_lower:
            # check if letter is in consonant list
            if letter in consonants:
                # increment counter
                counter += 1

        # if word has counter:
        #   append word to word_list
        if counter == n:
            word_list.append(word)

    return word_list
