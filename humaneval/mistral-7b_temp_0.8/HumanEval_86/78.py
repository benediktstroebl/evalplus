
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
    list_of_chars = []
    list_of_words = []
    list_of_ascii_values = []
    for i in s:
        list_of_chars.append(i)

    for i in range(len(list_of_chars)):
        list_of_ascii_values.append(ord(list_of_chars[i]))

    for i in range(len(list_of_chars)):
        list_of_words.append(list_of_chars[i])

    list_of_ascii_values.sort()
    list_of_words.sort()

    for i in range(len(list_of_ascii_values)):
        list_of_chars[i] = chr(list_of_ascii_values[i])

    for i in range(len(list_of_words)):
        s = list_of_words[i]

    return s
