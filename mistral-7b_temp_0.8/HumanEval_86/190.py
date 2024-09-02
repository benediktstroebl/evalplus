
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

    # input string
    s = "Hello World!!!!"

    # empty string to store the result
    res = ""

    # split string by space to get words
    words = s.split(" ")

    # loop through words
    for word in words:
        # initialize a new word
        newWord = ""

        # loop through characters of word
        for c in word:
            # append character in new word after sorting
            newWord = newWord + sorted(c)[0]

        # append space between words
        res = res + newWord + " "

    # remove last space
    res = res[:-1]

    return res
