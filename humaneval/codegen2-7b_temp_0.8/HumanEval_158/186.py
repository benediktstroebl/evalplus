
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if words is None:
        return ""

    max = ""
    unique_words = set()
    for word in words:
        if word not in unique_words:
            max = word
            unique_words.add(word)
        else:
            max = max if len(max) < len(word) else word
    return max

