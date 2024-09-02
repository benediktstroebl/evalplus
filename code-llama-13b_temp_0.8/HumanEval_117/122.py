
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
    # create a new list to store the selected words
    selected = []
    # check for empty string 
    if s == "":
        # return empty list
        return selected
    # get the list of words in the string
    words = s.split()
    # iterate over all the words
    for word in words:
        # check for vowels and consonants
        if sum([word.count(i) for i in 'aeiou']) == n:
            # add to list of selected words
            selected.append(word)
    # return the list of selected words
    return selected
