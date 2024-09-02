
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
    # Your code here

    # One way to do this is to convert the string to a list of words and
    # then rearrange the characters in each word to be in ascending order
    # using the sort function
    words = s.split()
    sorted_words = sorted(words, key=lambda x: sum(ord(c) for c in x))
    return ' '.join(sorted_words)
