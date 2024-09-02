
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

    if not s:
        return ''

    # get all words and blank spaces
    words = [word for word in s.split(' ') if word]
    spaces = [word for word in s.split(' ') if not word]

    # go through all words and put them in asc order
    words.sort(key=lambda word: ''.join(sorted(word)))

    # put the words back together
    return''.join(spaces + words)


