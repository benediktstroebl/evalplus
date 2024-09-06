
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
    string = s.lower()
    word_list = []
    word_index = 0
    for char in string:
        if char.isalpha():
            word_list.append(chr(ord(char) - 32)) # convert char to int, get ascii value, and add 32 to it
            while word_list[word_index] == chr(ord(char) - 32):
                word_index += 1
            word_index += 1
        else:
            if word_list:
                word_list.append(word_index)
                word_index = 0
    return ''.join(reversed(word_list))