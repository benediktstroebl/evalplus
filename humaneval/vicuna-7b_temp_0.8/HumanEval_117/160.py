
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
    # remove spaces
    s = s.lower().replace(' ', '')

    # split the string into a list of words
    words = s.split()

    # create an empty list to store the words
    result = []

    # loop through each word in the list
    for word in words:
        # check if the word contains exactly n consonants
        if len(word) == n and sum(map(lambda x: x.is_consonant(), word)) == n:
            # if the word passes the test, append it to the result list
            result.append(word)

    return result