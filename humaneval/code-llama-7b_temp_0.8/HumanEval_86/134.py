
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
    ret = []
    for word in s.split():
        # if blank space in s, append only blank space to ret
        if not word:
            ret.append(word)
        # else, join the characters in word in ascending order to new word and append it to ret
        else:
            ret.append("".join(sorted(word)))
    return " ".join(ret)
