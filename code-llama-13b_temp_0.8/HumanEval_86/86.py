
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
    if len(s) == 0 or len(s) == 1:
        return s
    output = []
    s = s.split(' ')
    for i in s:
        if len(i) == 0 or len(i) == 1:
            output.append(i)
        else:
            char_list = sorted(i)
            new_word = ''
            for j in char_list:
                new_word += j
            output.append(new_word)

    return ' '.join(output)

