
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
    # Your code here

    # Solution
    # split the string into a list of words
    words = s.split()

    # create an empty list
    result = []

    # loop over the words in the list
    for word in words:
        # split the word into a list of letters
        letters = list(word)

        # count the consonants
        count_cons = 0
        for letter in letters:
            # if the letter is a consonant
            if letter in CONSONANTS:
                # add 1 to the consonant count
                count_cons += 1

        # if the count matches the given number
        if count_cons == n:
            # add the word to the result list
            result.append(word)

    # return the result list
    return result
