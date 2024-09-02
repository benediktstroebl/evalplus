
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
    #Sanity check
    if s.isalpha() == False:
        return []

    #Create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    #Initialize a variable to store the number of vowels
    n_vowels = 0
    #Initialize a list to store the words with n consonants
    words = []
    #Split the string into a list of words
    s_list = s.split()

    #Count the number of vowels in each word
    for word in s_list:
        for letter in word:
            if letter.lower() in vowels:
                n_vowels += 1
        #If the number of vowels is less than n, append the word to the list
        if n_vowels < n:
            words.append(word)
        #Reset the number of vowels
        n_vowels = 0

    #Return the list of words
    return words
