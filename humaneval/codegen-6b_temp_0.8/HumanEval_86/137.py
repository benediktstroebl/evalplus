
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
    content = s.split()
    return ' '.join(sorted(content, key=lambda x: int(''.join(sorted(x)))[::-1]))
    # This is the second solution
    # Item1: use the sorted function to achieve this
    # Item2: loop of string
    # Item3: separate each string with ' '
    # Item4: use join to convert list to string
    # Item5: return string

