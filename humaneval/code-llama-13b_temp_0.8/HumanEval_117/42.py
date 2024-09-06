
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
    # Planning:
    # 1. Determine what data we already have
    # - s is a string (given)
    # - n is a natural number (given)
    # - we need to return a list of all words from s that contain exactly n consonants, 
    # in order these words appear in the string s.
    # - if the string s is empty then the function should return an empty list
    # - we may assume the input string contains only letters and spaces
    # - to keep it simple, define:
    #   - consonant as a letter that is not "a", "e", "i", "o", or "u"
    #   - word as a sequence of letters separated by a space
    # 2. Determine what we need to do:
    # - check if s is empty
    #   - if so, return an empty list
    # - make a list to hold the results
    # - for each word in s, determine if it contains exactly n consonants
    #   - if so, add it to the list
    # - return the list
    # 3. Translate those steps into Python

    # check if s is empty
    if len(s) == 0:
        # if so, return an empty list
        return []
    # make a list to hold the results
    results = []
    # for each word in s, determine if it contains exactly n consonants
    for word in s.split():
        # count the consonants
        counter = 0
        for letter in word:
            if letter not in "aeiou":
                counter += 1
        # if so, add it to the list
        if counter == n:
            results.append(word)
    # return the list
    return results

