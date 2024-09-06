
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
    # Convert string to lowercase
    s = s.lower()

    # Split string into words
    words = s.split()

    # Reverse the order of characters in each word
    words = [(chr(ord(c) ^ 0x5f), c) for c in words[1:]]

    # Reverse the order of words
    words = words[::-1]

    # Join the words and blank spaces back into a string
    return ' '.join(words)
