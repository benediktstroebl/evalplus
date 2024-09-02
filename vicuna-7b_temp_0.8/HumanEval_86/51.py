
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
    # Convert all characters in string to lowercase
    s = s.lower()
    # Remove all blanks in string
    s = s.strip()
    # Split the string into a list of words
    words = s.split()
    # Sort the list of words in ascending order based on their ASCII values
    words = sorted(words, key=lambda x: ord(x))
    # Join the list of words together into a new string
    return ' '.join(words)
