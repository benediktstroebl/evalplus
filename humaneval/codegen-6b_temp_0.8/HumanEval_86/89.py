
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
    # Solved, works but not faster than
    # temp = []
    # for word in s.split():
    #     temp.append(''.join(sorted(word)))
    # return ' '.join(temp)

    # Solved but still not fast enough
    temp = list(s.split())
    temp.sort(key=lambda item: ''.join(sorted(item)))
    return ' '.join(temp)

