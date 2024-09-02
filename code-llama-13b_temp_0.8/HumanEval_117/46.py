
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
    # plan:
    # - use string methods to get a list of all the words.
    # - use a for loop to go through the words.
    # - use a while loop to count the number of consonants in the word
    # - add the word to the result list if the consonant count is correct.
    
    # create the list of words:
    list_of_words = s.split()
    
    # initialize a list to store the result:
    result = []
    
    # use a for loop to go through the list of words:
    for word in list_of_words:
        
        # initialize a counter for consonants
        counter = 0
        
        # initialize a for loop to go through the word letter by letter:
        for letter in word:
            if letter not in "aeiou":
                counter += 1
        
        # if the counter is correct, add the word to the result list
        if counter == n:
            result.append(word)
        
    # return the result list:
    return result


