
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    best_so_far = ""
    best_so_far_count = -1

    for word in words:
        count = unique(word)
        if count > best_so_far_count:
            best_so_far = word
            best_so_far_count = count
        elif count == best_so_far_count and word < best_so_far:
            best_so_far = word

    return best_so_far
