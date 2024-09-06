
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
    if s == '':
        return ''
    # split by space to get all words
    words = s.split(' ')
    # get all words
    words_list = []
    for word in words:
        if word == '':
            words_list.append('')
            continue
        # sort each word and add to list
        word_list = list(word)
        word_list.sort()
        word_shuffle = ''.join(word_list)
        words_list.append(word_shuffle)
    # join words back together
    words_shuffle = ' '.join(words_list)
    return words_shuffle

