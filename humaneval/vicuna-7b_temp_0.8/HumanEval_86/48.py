
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
    # You can use string slicing to change order of characters in string
    # slicing(0,len(s)-1) to get all characters in reverse order
    # slicing(0,len(s)) to get all characters in forward order
    # But to keep words and spaces in the same order, you need to use slicing
    # in combination with string concatenation and extraction
    return ' '.join([s[i:j] for i,j in zip(range(len(s)-1),range(len(s),len(s)))])
