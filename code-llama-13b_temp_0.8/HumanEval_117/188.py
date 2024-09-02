
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
    # identify consonants in string
    # create a list of the identified consonants
    # identify words that only contain the consonants in the list
    # return words that contain only the identified consonants
    
    # create list of consonants
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    # create list of words
    words = s.split()
    # create a list of words containing only the identified consonants
    result = []
    # return words that contain only the identified consonants
    for word in words:
        word_consonants = []
        for char in word:
            if char.lower() in consonants:
                word_consonants.append(char.lower())
        if len(word_consonants) == n:
            result.append(word)
    return result
