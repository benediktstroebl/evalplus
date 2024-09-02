
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
    # split the string into a list of words
    # iterate through list of words, and check if word meets criteria
    # return list of words that meet criteria
    
    #create empty list
    word_list = []
    
    #split the string into a list of words
    split_string = s.split()
    
    #iterate through list of words, and check if word meets criteria
    #for each word:
    for word in split_string:
        #remove first and last letter
        trimmed_word = word[1:-1]
        #remove spaces
        no_spaces = trimmed_word.replace(" ", "")
        #remove vowels
        no_vowels = no_spaces.replace("a", "")
        no_vowels = no_vowels.replace("e", "")
        no_vowels = no_vowels.replace("i", "")
        no_vowels = no_vowels.replace("o", "")
        no_vowels = no_vowels.replace("u", "")
        #count the number of consonants in word
        count = len(no_vowels)
        #check if number of consonants in word equals n
        if count == n:
            #add word to word_list
            word_list.append(word)
            
    #return list of words that meet criteria
    return word_list
