
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dict = {}
    max_value = 0
    max_key = ""
    for word in words:
        dict[word] = len(set(word))
        if dict[word] > max_value:
            max_value = dict[word]
            max_key = word
    return max_key





