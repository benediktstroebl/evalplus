
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return words[0] if len(set(words[0])) > len(set(words[1])) else words[1]

    sorted_list = sorted(words, key=lambda x: len(set(x)))
    sorted_list_length = [len(set(x)) for x in sorted_list]
    if sorted_list_length[0] == sorted_list_length[1]:
        sorted_list = sorted(words)
        return sorted_list[0]
    return sorted_list[sorted_list_length.index(max(sorted_list_length))]
