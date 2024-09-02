
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
    # Ordered string.
    ordered_string = ''
    # A list to store the ordered words.
    ordered_words = []
    # Split the string into words.
    words = s.split()
    # Iterate over the words.
    for word in words:
        # Sort the word.
        ordered_string = ''.join(sorted(word))
        # Add the ordered word to the list.
        ordered_words.append(ordered_string)
    # Join the words in the list.
    return ' '.join(ordered_words)
