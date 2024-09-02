
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = []
    max_words = []
    for word in words:
        if len(set(word)) == len(word):
            max_chars.append(word)
            max_words.append(word)
        else:
            max_chars.append(word)
            max_words.append(word)
    if len(set(max_chars)) == len(max_chars):
        return max_chars[0]
    else:
        return max_words[0]
