
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dict = {}
    for word in words:
        val = len(set(word))
        if val in dict:
            dict[val].append(word)
        else:
            dict[val] = [word]
    # print(dict)
    size = max(dict, key=lambda x: len(dict[x]))
    # print(size)
    return dict[size].pop()

