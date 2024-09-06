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
    # Use a regex to find all words (sequences of non-space characters)
    words = re.findall(r'\S+', s)
    
    # Sort each word based on ascending ASCII value
    sorted_words = [char for char in sorted(words, key=lambda x: x.lower())]
    
    # Add space characters back to form the new ordered string
    return ' '.join(sorted_words)