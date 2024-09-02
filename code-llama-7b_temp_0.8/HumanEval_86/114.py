
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

    # Check that s is a string
    if type(s) != str:
        return 'Error: Input is not a string'

    # Check that s is non empty
    if s == '':
        return 'Error: Input is empty'

    # Split sentence in words
    words = s.split()
    new_words = []
    # Create new words using anti shuffle
    for word in words:
        if word == '':
            new_words.append(' ')
        else:
            new_words.append(''.join(sorted(word)))

    # Return the new sentence
    return ' '.join(new_words)

