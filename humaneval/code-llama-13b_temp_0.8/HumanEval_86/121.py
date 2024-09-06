
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
    sorted_str = ''
    for char in s:
        if char != ' ':
            sorted_str += char
        else:
            sorted_str += char

    sorted_list = []
    temp_str = ''
    for char in sorted_str:
        if char == ' ':
            sorted_list.append(temp_str)
            temp_str = ''
        else:
            temp_str += char
    sorted_list.append(temp_str)

    sorted_list.sort(key=lambda x: ''.join(sorted(x)))
    print sorted_list

    new_sorted_str = ''
    for i, word in enumerate(sorted_list):
        if i == 0:
            new_sorted_str += word
        else:
            new_sorted_str += ' ' + word

    return new_sorted_str

