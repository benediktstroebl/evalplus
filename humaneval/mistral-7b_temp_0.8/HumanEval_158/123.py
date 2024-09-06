
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    count = {}
    max_len = 0
    max_string = ""
    for word in words:
        count[word] = len(set(word))
        if count[word] > max_len:
            max_len = count[word]
            max_string = word

    return max_string
