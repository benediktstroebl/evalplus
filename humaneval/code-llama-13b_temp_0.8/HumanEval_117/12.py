
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
    # Plan:
    # set consonant string
    # for each word, create letter list
    # get index of first letter
    # compare number of consonants with n
    # if match, append to list
    # return list
    consonants = 'bcdfghjklmnpqrstvwxz'
    word_list = s.split(' ')
    index = 0
    new_list = []
    for word in word_list:
        letter_list = list(word)
        index = 0
        count = 0
        while index < len(letter_list):
            if letter_list[index] in consonants:
                count += 1
            index += 1
        if count == n:
            new_list.append(word)
    return new_list
