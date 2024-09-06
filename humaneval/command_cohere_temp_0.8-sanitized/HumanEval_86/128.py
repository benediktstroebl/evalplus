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
    # Use a regex to find all words (assumes words are separated by spaces)
    words = re.findall(r'\w+', s)
    
    # Iterate through each word and sort the characters
    ordered_words = [ chr(c) for c in sorted(list(set(word))) for word in words]
    
    # Zip the sorted letters into a single string and return
    return ' '.join(ordered_words)