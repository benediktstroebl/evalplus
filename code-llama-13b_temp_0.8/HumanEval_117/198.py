
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
    # set up an empty list to append words with n consonants to
    # iterate through string
        # check if letter is a consonant
            # if true, increment counter by 1
            # if false, reset counter to 0
        # if counter == n
            # add word to list
        # else, continue
    # return list
    
    # set up empty list to append words with n consonants to
    list_of_words = []
    
    # iterate through string
    for i in range(len(s)):
        # check if letter is a consonant
        if s[i] not in "aeiou":
            # if true, increment counter by 1
            counter = 1
            # if false, reset counter to 0
        else:
            counter = 0
        
        # if counter == n
        if counter == n:
            # add word to list
            list_of_words.append(s[i])
        # else, continue
        else:
            continue
    # return list
    return list_of_words
