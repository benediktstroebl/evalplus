
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""
    max_len = max([len(word) for word in words])
    max_word = [word for word in words if len(word) == max_len]
    if not max_word:
        return ""
    elif max_word[0].lower() > max_word[1].lower():
        return max_word[0]
    else:
        return max_word[1]
