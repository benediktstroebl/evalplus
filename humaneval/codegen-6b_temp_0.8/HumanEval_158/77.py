
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word = ""
    max_count = 0
    for word in words:
        if len(set(word)) > max_count:
            max_count = len(set(word))
            max_word = word
    return max_word


assert find_max(["name", "of", "string"]) == "string"
assert find_max(["name", "enam", "game"]) == "enam"
assert find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
assert find_max(["aaaaa", "aab", "bca"]) == "aab"
assert find_max(["dsa", "aidy", "sasa"]) == "dsa"
