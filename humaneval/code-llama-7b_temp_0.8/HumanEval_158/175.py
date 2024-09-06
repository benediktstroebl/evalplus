
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    uniques_list = []
    for word in words:
        uniques = []
        for letter in word:
            if letter not in uniques:
                uniques.append(letter)
        uniques_list.append(uniques)
    max_uniques = 0
    max_index = 0
    for index, uniques in enumerate(uniques_list):
        if len(uniques) > max_uniques:
            max_uniques = len(uniques)
            max_index = index
    return words[max_index]

