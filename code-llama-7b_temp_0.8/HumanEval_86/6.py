
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
        return s
    else:
        s_list = s.split(' ')
        word_list = []
        for word in s_list:
            if word == '':
                word_list.append(word)
            else:
                char_list = []
                for char in word:
                    char_list.append(char)
                char_list.sort()
                word_list.append(''.join(char_list))
        return ' '.join(word_list)
