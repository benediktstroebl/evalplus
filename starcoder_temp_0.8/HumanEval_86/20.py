
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

    if not s:
        return s

    word_list = s.split(' ')

    # Put words in a set
    word_set = set()
    for word in word_list:
        word_set.add(word)

    # Create a map between words and ordered words
    # O(n * k)
    word_map = {}
    for word in word_set:
        word_map[word] = sorted(word)

    # Replace words in the string
    # O(n * k)
    for i in range(len(word_list)):
        word_list[i] = word_map[word_list[i]]

    return ''.join(word_list)
