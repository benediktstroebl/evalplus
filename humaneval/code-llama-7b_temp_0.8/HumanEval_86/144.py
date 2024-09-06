
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

    if s == None or len(s) == 0:
        return s

    shuffled_words = s.split(' ')

    result = ""

    for word in shuffled_words:
        word = word.strip()
        if len(word) == 0:
            result += word
        else:
            new_word = sorted(word)
            result += "".join(new_word) + " "

    return result[:-1]
