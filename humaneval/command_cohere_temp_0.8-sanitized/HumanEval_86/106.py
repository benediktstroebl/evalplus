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
    # Use a regex to capture all words separately
    words = re.findall(r'\w+', s)
    new_word = ''.join(sorted(word))
    # Replace all words with the new word and return the updated string
    s = re.sub(r'\b\w+\b', new_word, s)
    return s