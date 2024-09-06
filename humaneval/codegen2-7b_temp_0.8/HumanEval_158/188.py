
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
        return ''
    if len(words) == 1:
        return words[0]
    words_new = []
    for w in words:
        if w in words_new:
            continue
        else:
            words_new.append(w)
    if words_new == []:
        return ''
    return words_new[0]
