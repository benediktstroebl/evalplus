
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

    # find list of words in s
    words = s.split()
    
    # list to store words that meet criteria
    list_of_words = []

    # check each word in list of words
    for word in words:

        # counter to store the number of consonants
        count = 0

        # loop through each letter in word
        for letter in word:

            # check if letter is a consonant
            if letter.lower() not in vowels:
                count += 1

        # check if count of consonants is equal to parameter n
        if count == n:
            list_of_words.append(word)

    # return list of words that meet criteria
    return list_of_words
