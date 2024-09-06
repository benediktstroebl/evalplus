
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def get_uniqe(word):
        return set(word)

    def get_count(word):
        return len(set(word))

    result = words[0]
    for word in words:
        if get_count(word) > get_count(result):
            result = word
    return result

