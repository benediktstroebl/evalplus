
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
    # My code
    # return " ".join(sorted(s.split(), key=lambda x: "".join(sorted(x))))

    # My code
    # s = s.split()
    # return " ".join(sorted(s, key=lambda x: "".join(sorted(x))))

    # Rohan's code
    # s = s.split()
    # result = ""
    # for word in s:
    #     result += sorted(word) + " "
    # return result[:-1]

    # Rohan's code
    return " ".join([sorted(word) for word in s.split()])

