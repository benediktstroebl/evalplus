
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

    #represents the words 
    #words = []
    #n_consonants = 0
    #c_words = []

    #break up the string into a list of words
    s = s.split()

    #loop through each word in the string
    for word in s:
        #count the number of consonants
        n_consonants = 0
        for c in word:
            if c not in "aeiou":
                n_consonants += 1
        
        #if the number of consonants is equal to the number the user wants
        if n_consonants == n:
            #add the word to the list
            #words.append(word)
            return word
            #print(word)

    #return the list
    #return words
