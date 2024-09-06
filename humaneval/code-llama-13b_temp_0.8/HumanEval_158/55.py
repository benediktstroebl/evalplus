
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_map = {}
    for word in words:
        if not unique_map.get(word, False):
            unique_map[word] = len(set(word))
    max_value = max(unique_map.values())
    result = []
    for word in unique_map:
        if unique_map[word] == max_value:
            result.append(word)
    return result[0]
