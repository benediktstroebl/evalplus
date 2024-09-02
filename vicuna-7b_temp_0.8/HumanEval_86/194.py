
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
    # Convert the string to lowercase
    s = s.lower()

    # Split the string into words
    words = s.split()

    # Shuffle the words in ascending order based on their ASCII values
    shuffled_words = sorted(words, key=lambda x: ord(x))

    # Concatain the shuffled words back into a new string
    new_s = ' '.join(shuffled_words)

    return new_s