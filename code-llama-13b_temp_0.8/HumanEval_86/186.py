
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
    shuffle_dict = {}
    for char in s:
        if char in shuffle_dict:
            shuffle_dict[char] += 1
        else:
            shuffle_dict[char] = 1
    sorted_char_list = []
    for item in sorted(shuffle_dict.items(), key=lambda x: x[0]):
        for _ in range(item[1]):
            sorted_char_list.append(item[0])
    return ''.join(sorted_char_list)
