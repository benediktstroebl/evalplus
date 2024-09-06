
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
    
    def contains_n_consonants(word, n):
        # we need to define a function that check if a word contains exactly n consonants
        # in order to be able to call it from select_words
        count = 0
        # go through each character in the word
        for letter in word:
            # if letter is not a vowel
            if letter.lower() not in 'aeiou':
                count += 1
            if count == n:
                return True
        return False
    
    # initialize a list to hold all the words that contain exactly n consonants
    words = []
    # go through each word in the string
    for word in s.split():
        # check if the word contains exactly n consonants
        if contains_n_consonants(word, n):
            # if so, add the word to the list
            words.append(word)
    # return the list
    return words
