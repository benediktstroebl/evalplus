
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # use a set to store the characters and their index
    # then use a dictionary to store the characters and its ascending order
    # then use a list to store the words
    # then use a dictionary to store the words and its index
    # then use a list to store the words in ascending order

    #convert string to list of characters
    words = s.split()

    #convert list of characters to set of characters
    chars = set(words)

    #convert set of characters to dictionary of characters and its index
    char_dict = {c: i for i, c in enumerate(chars)}

    #convert list of words to list of words in ascending order
    words_order = list(zip(*(sorted(list(zip(words, range(len(words)))))[::-1]))[::-1])

    #convert list of words in ascending order to string
    return ' '.join(words_order)