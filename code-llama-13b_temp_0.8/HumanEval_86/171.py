
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
    # return ''.join(sorted(s)) # This is much more simple and effective

    # 1. Split s by spaces
    # 2. Sort each word by its characters
    # 3. Join words with a space in between

    # 1
    words = s.split()
    # 2
    sorted_words = [sorted(word) for word in words]
    # 3
    return ' '.join(sorted_words)

