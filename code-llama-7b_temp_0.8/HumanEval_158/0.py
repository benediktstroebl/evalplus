
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words = sorted(words)
    max_length = len(words[0])
    words_to_return = []
    for word in words:
        if len(set(word)) == max_length:
            words_to_return.append(word)
    if len(words_to_return) == 0:
        return ""
    else:
        return words_to_return[0]
