
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return None
    max_count, best = 0, words[0]
    for word in words:
        count = len(set(word))
        if count > max_count:
            max_count = count
            best = word
        elif count == max_count:
            if word < best:
                best = word
    return best
