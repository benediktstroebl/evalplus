
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
    # check length of word
    # if n is not in word return empty list
    # if n is in word add word to list
    # return list of words
    
    # lists to hold words
    list_of_words = []
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    # loop through words in string
    for word in s.split():
        # create counter for consonants
        count = 0
        # check if any letters in word are not vowels
        for letter in word.lower():
            # if letter is in consonants list
            if letter in consonants:
                # increment consonant count
                count += 1
        # if n is equal to count
        if count == n:
            # append word to list
            list_of_words.append(word)
    # return list of words
    return list_of_words
