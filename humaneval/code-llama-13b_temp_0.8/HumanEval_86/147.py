
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

    # results = []
    # s_split = s.split(" ")
    # for word in s_split:
    #     word = ''.join(sorted(word))
    #     results.append(word)
    # return " ".join(results)
    return " ".join(map(lambda w: ''.join(sorted(w)), s.split(' ')))

