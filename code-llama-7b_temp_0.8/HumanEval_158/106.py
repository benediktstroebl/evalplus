
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    count = 0
    max_count = 0
    current = ""
    for word in words:
        if len(word) > count:
            count = len(word)
            current = word
        else:
            pass

        if len(word) == count:
            if current > word:
                current = word
            else:
                pass

        if max_count < count:
            max_count = count

    return current
