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
    # Use a regex to capture all words separated by space.
    # Sort the list of characters and join them to form a new word.
    # Iterate through each word in the string and replace them with the new word.
    words = [char for char in s.split()]
    new_word = ''.join(sorted(words))
    return ' '.join(word if word != new_word else new_word for word in s.split())