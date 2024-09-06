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
    # Sort the words based on the ASCII value of the first character
    words = [word for word in words if word]
    words = sorted(words, key=lambda x: x[0].lower())
    # Join them back to form a single string
    joined_words = ' '.join(words)
    return s if joined_words == s else joined_words