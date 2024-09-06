
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
        return s
    
    # Split the string into words
    words = s.split()
    
    # Reverse the order of characters in each word
    words = [word[::-1] for word in words]
    
    # Concat the reversed words back to a new string
    return ' '.join(words)