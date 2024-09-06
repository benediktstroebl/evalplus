
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique = {}
    result = ""
    for word in words:
        for letter in word:
            if letter not in unique:
                unique[letter] = 1
            else:
                unique[letter] += 1
        if len(unique) > len(result):
            result = word
        elif len(unique) == len(result) and word < result:
            result = word
        unique.clear()
    return result

