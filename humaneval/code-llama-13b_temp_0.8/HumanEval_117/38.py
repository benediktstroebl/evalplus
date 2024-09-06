
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
    
    # plan: create a function that returns a list of words, then call this function with a
    # parameter n and return a list of words that contain exactly n consonants in them
    
    def list_of_words(s):
        # function that returns a list of words
        
        words = []
        # initialize a list that will contain the words
        
        for word in s.split():
            # for loop that loops through the list of words
            
            words.append(word)
            # appends each word in the list of words to the list words
            
        return words
        
        # returns a list of words
    
    def contains_n_consonants(words, n):
        # function that returns a list of words that contain exactly n consonants
        
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        # list of consonants
        
        result = []
        # initialize a list that will contain the words that contain exactly n consonants
        
        for word in words:
            # for loop that loops through the list of words
            
            count = 0
            # initialize a variable that will count the number of consonants
            
            for letter in word:
                # for loop that loops through the letters in a word
                
                if letter.lower() in consonants:
                    # if the letter is a consonant
                    
                    count += 1
                    # increment the counter
                    
            if count == n:
                # if the number of consonants is equal to n
                
                result.append(word)
                # append the word to the list result
            
        return result
        # returns a list of words that contain exactly n consonants
        
    return contains_n_consonants(list_of_words(s), n)
    # returns a list of words that contain exactly n consonants
