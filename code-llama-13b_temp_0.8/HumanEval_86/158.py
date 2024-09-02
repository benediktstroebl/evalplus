
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

    # Your code here
    def anti_shuffle_word(word):
        word_list = []
        for i in range(len(word)):
            word_list.append(word[i])
        word_list.sort()
        word_sorted = ''
        for i in range(len(word_list)):
            word_sorted += word_list[i]
        return word_sorted

    s_list = s.split()
    s_sorted = ''
    for i in range(len(s_list)):
        word = s_list[i]
        word_sorted = anti_shuffle_word(word)
        s_sorted += word_sorted
        if i != len(s_list) - 1:
            s_sorted += ' '

    return s_sorted

