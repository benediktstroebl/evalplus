
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_str = ""
    for word in words:
        if max_str == "":
            max_str = word
        else:
            if len(word) > len(max_str):
                max_str = word
            elif len(word) == len(max_str):
                if word < max_str:
                    max_str = word
    return max_str

