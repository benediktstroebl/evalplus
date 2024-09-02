
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
    #loop through the string
    words = []
    word = ""
    for c in s:
        #if we're at a space, store the word
        if c == " ":
            words.append(word)
            word = ""
        #if we're not at a space, add the character to our word
        else:
            word = word + c
    
    #trim the word list
    word_list = []
    for w in words:
        #split the word into letters
        letters = list(w)
        #count the consonants
        consonants = 0
        for l in letters:
            if l == "a" or l == "e" or l == "i" or l == "o" or l == "u" or l == " ":
                consonants = consonants + 1
        #if the word has the right amount of consonants, add it to the word list
        if consonants == n:
            word_list.append(w)
    
    #return the word list
    return word_list
