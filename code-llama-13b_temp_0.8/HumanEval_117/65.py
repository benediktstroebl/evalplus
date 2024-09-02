
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
    # - break string into words
    # - check each word for n consonants
    # - add each word to list, and return
    
    # init a list to hold words with n consonants
    words_with_n_consonants = []
    
    # break string into words
    list_of_words = s.split()
    
    # check each word for n consonants
    for word in list_of_words:
        num_of_consonants = 0
        for letter in word:
            if letter not in "aeiouAEIOU":
                num_of_consonants += 1
        if num_of_consonants == n:
            words_with_n_consonants.append(word)
            
    return words_with_n_consonants
    
