
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
    # the n of consonants in a word
    word_n = 0
    # the n of consonants in the string
    str_n = 0
    result = []
    
    # to separate each word into a list
    words = s.split(" ")
    # to check if a word has only 1 character, which is whitespace
    # if a word has only one character, then it must be whitespace
    for i in range(len(words)):
        if words[i].isspace():
            words.remove(words[i])
            
    # to check each word in the list
    for word in words:
        # to check each character in a word
        for char in word:
            if char.lower() in "bcdfghjklmnpqrstvwxyz":
                word_n += 1
        # to check if a word contains n consonants
        if word_n == n:
            result.append(word)
        word_n = 0
    
    return result
