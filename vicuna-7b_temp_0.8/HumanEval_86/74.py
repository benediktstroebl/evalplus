
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
    # We use a regular expression to match each word and capture its characters in a group
    # We use the ord function to get the ASCII value of each character and then we arrange them in ascending order
    # We concatenate all the groups together to form a new word
    return ''.join([re.sub(r'\w+', lambda x: ''.join([chr(ord(c) + 1) for c in x]), s) for s in re.split('[\W]', s) if s])
