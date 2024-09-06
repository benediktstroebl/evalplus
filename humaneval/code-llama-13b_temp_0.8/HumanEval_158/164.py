
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique = []
    for string in words:
        uniq = []
        for char in string:
            if char not in uniq:
                uniq.append(char)
        unique.append((len(uniq), string))
    return sorted(unique)[-1][1]
