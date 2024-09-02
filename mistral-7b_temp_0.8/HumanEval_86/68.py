
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
    def is_string_number(s):
        return s.isdigit()

    def remove_punctuation(s):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        return ''.join(ch for ch in s if ch not in punctuations)

    def is_word(s):
        return remove_punctuation(s).strip().isalpha()

    def is_number(s):
        return s.isdigit()

    if is_string_number(s):
        return s
    s = s.replace(' ', '')
    if is_word(s):
        return sorted(s)
    word_list = s.split(' ')
    for i in range(len(word_list)):
        if is_word(word_list[i]):
            word_list[i] = sorted(word_list[i])
    return ' '.join(word_list)

