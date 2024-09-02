
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
    # IMPORTANT: READ HELP INFO AND STUDENT COMMENTS BEFORE STARTING!

    # 1. Split the string s into a list of words, ignoring the spaces
    # 2. sort the words
    # 3. join the sorted words into a string and return

    # HELP INFO:
    # Look at the solution.
    # If you have any question, please write them as comment in the solution.

    # STUDENT COMMENTS:
    # 1. you should use the .split() method to turn a string into a list of strings.
    # 2. you should use the .join() method to turn a list of strings into a string.

    return " ".join([sort_string(word) for word in s.split()])
