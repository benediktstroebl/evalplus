
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    words_set = set()
    result = ""
    for word in words:
        if word in words_set:
            continue
        else:
            words_set.add(word)
            if len(word) > len(result):
                result = word
            elif len(word) == len(result):
                if word < result:
                    result = word
    return result

