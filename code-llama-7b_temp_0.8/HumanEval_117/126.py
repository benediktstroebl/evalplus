
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

    # strip the string and store it
    s = s.strip()
    
    # create a list of all the words in the string
    words = s.split()

    # create a list to store the words that contain exactly n consonants
    answer = []

    # loop through all the words
    for word in words:
        # create a set from the word
        word_set = set(word)
        
        # check if the set has less than 2 elements
        if len(word_set) < 2:
            continue

        # loop through the set
        for letter in word_set:
            # check if the letter is a consonant
            if letter in "bcdfghjklmnpqrstvwxyz":
                continue
            
            # if the letter is not a consonant
            else:
                # break out of the for loop
                break

        # if the word contains only consonants
        else:
            # if the length of the word is equal to the parameter n
            if len(word) == n:
                # add the word to the answer list
                answer.append(word)

    # return the answer list
    return answer

