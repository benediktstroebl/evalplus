
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word = ""
    max_chars = 0
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_chars:
            max_chars = unique_chars
            word = word.lower()
    return word

words = ["name", "enam", "game", "aaa", "bb"]
print(find_max(words))