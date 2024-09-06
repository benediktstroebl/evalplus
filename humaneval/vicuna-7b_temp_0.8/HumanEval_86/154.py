
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
    # convert string to lowercase
    s = s.lower()
    # create empty string to store result
    result = ''
    # iterate through each character in the string
    for c in s:
        # check if current character is alphabetic
        if c.isalpha():
            # add the ascii value of the character to the result
            result += str(c.lower() + ord('a') - 1)
        else:
            # if it's not alphabetic, add it as is
            result += str(c)
    return result
