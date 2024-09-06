
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
    for word in words:
        unique[word] = len(set(word))
    max_word = max(unique, key=unique.get)
    for word in words:
        if len(word) == len(max_word):
            if word == max_word:
                continue
            else:
                return ""
    return max_word

