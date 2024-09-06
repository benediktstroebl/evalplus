
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
    words = s.split()
    shuffle_words = []
    for word in words:
        shuffle_word = ""
        for c in word:
            shuffle_word += chr(ord(c)+32)
        shuffle_words.append(shuffle_word)

    shuffle_words.sort()

    return " ".join(shuffle_words)
