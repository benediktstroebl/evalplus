
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

    new_s = ""
    words = s.split(" ")
    ordered_words = []
    ordered_letters = []
    for word in words:
        for c in word:
            ordered_letters.append(c)
    ordered_letters.sort()
    for l in ordered_letters:
        new_s += l
    new_s += " "
    for word in words:
        new_s += word
    return new_s

