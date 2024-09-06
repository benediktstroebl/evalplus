
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
    # We can divide the string into a list of words, then for each word,
    # order it in ascending order of ascii, then join it back together.
    # We can even do this in one line:
    # return " ".join(["".join(sorted(word)) for word in s.split()])

    # But we can do it in two lines, first split it, then order it,
    # and finally join it back together.
    word_list = s.split()
    ordered_word_list = [
        "".join(sorted(word)) for word in word_list]

    return " ".join(ordered_word_list)
