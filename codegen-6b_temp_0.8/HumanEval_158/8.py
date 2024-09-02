
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    sortbylen = sorted(words, key=len)
    return sortbylen[-1]

assert find_max(["name", "of", "string"]) == "string"
assert find_max(["name", "enam", "game"]) == "enam"
assert find_max(["aaaaaaa", "bb" ,"cc"]) == ""
assert find_max(["Abc", "cd", "Def", "ghi", "klm", "op", "stlm", "ts", "uv", "wxy"]) == "Abc"
assert find_max(["a", "b", "c", "a", "d", "b", "c"]) == "b"
