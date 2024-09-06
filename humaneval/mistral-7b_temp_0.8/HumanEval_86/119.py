
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
    alphabet_list = list(s)
    for i in range(0, len(alphabet_list)):
        smallest = alphabet_list[i]
        min_index = i
        for j in range(i + 1, len(alphabet_list)):
            if alphabet_list[j] < smallest:
                smallest = alphabet_list[j]
                min_index = j
        alphabet_list[i], alphabet_list[min_index] = alphabet_list[min_index], alphabet_list[i]
    return "".join(alphabet_list)
