
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    count = {}
    for word in words:
        if count.get(word, 0):
            count[word] += 1
        else:
            count[word] = 1

    max_len = max(count.values())
    return max(count, key=lambda x: (-count.get(x), x))

