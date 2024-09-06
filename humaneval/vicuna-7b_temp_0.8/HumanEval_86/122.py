
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
    # Check if the string is empty
    if not s:
        return ""

    # Split the string into words
    words = s.split()

    # Shuffle the characters of each word
    shuffled_words = [chars.upper() for chars in words]

    # Join the words with their shuffled characters
    return " ".join(shuffled_words)
