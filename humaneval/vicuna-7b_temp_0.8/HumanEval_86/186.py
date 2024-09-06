
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
    shuffled_words = []
    current_word = []
    for word in words:
        if len(word) > 0:
            current_char = chr(ord(word[0]) + len(shuffled_words[-1]))
            current_word.append(current_char)
        else:
            current_word.append(' ')
        shuffled_words.append(current_word)
        current_word = []
    return ' '.join(shuffled_words)