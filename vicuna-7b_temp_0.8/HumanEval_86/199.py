
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
    word_list = s.split()
    shuffled_list = []
    for i, j in itertools.product(range(len(word_list)), repeat=2):
        temp = ''.join(word_list[i:j+1])
        shuffled_list.append(temp)
    return ' '.join(shuffled_list)
