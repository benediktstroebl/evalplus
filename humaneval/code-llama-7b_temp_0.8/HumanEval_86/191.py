
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

    s_list = s.split(' ')
    ordered_list = []
    for word in s_list:
        if word != '':
            ordered_word = ''.join(sorted(word))
            ordered_list.append(ordered_word)
        else:
            ordered_list.append(word)
    return ' '.join(ordered_list)
