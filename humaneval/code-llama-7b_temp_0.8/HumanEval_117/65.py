
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
    # define a variable to store the list of words
    new_words = []
    # split the string into a list of words
    words = s.split()
    # use a for loop to iterate through each word
    for word in words:
        # use a for loop to iterate through each letter in the word
        for letter in word:
            # check if the letter is not a vowel
            if letter not in "aeiou":
                # check if the counter equals the number n
                if counter == n:
                    # append the word to the list of words
                    new_words.append(word)
                # increment the counter if the letter is not a vowel
                counter += 1
            # reset the counter if the letter is a vowel
            else:
                counter = 0
    # return the list of words
    return new_words
