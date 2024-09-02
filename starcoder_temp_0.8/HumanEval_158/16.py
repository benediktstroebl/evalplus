
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_count = 0
    max_word = ""
    for i in words:
        count = len(set(list(i)))
        if count > max_count:
            max_count = count
            max_word = i
        elif count == max_count:
            if i < max_word:
                max_word = i
    return max_word
