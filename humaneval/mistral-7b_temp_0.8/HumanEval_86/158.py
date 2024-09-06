
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
    split_words = s.split()
    anti_shuffle_words = []
    for i in range(len(split_words)):
        anti_shuffle_words.append("".join(sorted(split_words[i])))
    anti_shuffle_words = " ".join(anti_shuffle_words)
    return anti_shuffle_words
