
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word = ''
    max_num_char = 0
    for i in words:
        if len(i) > max_num_char:
            max_num_char = len(i)
            word = i
        elif len(i) == max_num_char:
            word = sorted([word, i])[0]
    return word

