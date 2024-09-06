
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
    # Take the string and separate it by spaces
    split_str = s.split(" ")
    # Reverse the string
    rev_str = split_str[::-1]

    reordered_str = ""
    for i in range(len(rev_str)):
        reordered_str += rev_str[i]
        if i != len(rev_str)-1:
            reordered_str += " "

    return reordered_str

