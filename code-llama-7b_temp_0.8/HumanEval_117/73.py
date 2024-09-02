
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
    # Return an empty list if s is an empty string.
    if s == "":
        return []

    # Make an empty list to store the words that are the correct length.
    word_list = []

    # Split s into a list of words.
    words = s.split()

    # Loop through the words in the list.
    for word in words:

        # Make an empty list to store the letters that are not vowels.
        letters_list = []

        # Loop through the letters in the word.
        for letter in word:

            # If the letter is not a vowel, add it to the letters list.
            if letter.lower() not in ["a", "e", "i", "o", "u"]:
                letters_list.append(letter)

        # If the length of the letters list is equal to the n, add the word to the word list.
        if len(letters_list) == n:
            word_list.append(word)

    # Return the list of words that are the correct length.
    return word_list

