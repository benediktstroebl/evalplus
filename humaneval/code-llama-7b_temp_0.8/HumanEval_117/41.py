
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
    # To begin, we need to get a list of the words in the string
    words_list = s.split()

    # Then we need to find all words that have n letters that are not vowels
    selected_words = []
    for word in words_list:
        # Count the number of consonants in a word
        consonants = 0
        for letter in word:
            if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
                pass
            else:
                consonants += 1

        # If the number of consonants is n, add the word to the list
        if consonants == n:
            selected_words.append(word)
    
    return selected_words
