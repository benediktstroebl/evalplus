
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
        return ""
    max_num, max_words = 0, []
    for word in words:
        if len(set(word)) > max_num:
            max_num = len(set(word))
            max_words = [word]
        elif len(set(word)) == max_num:
            max_words.append(word)

    return min(max_words)
