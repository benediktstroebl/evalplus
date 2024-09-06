
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    try:
        max_char = max([len(set(word)) for word in words])
    except ValueError:
        return ""

    words_with_max_char = [word for word in words if len(set(word)) == max_char]
    if len(words_with_max_char) > 1:
        return words_with_max_char[0]
    elif len(words_with_max_char) == 1:
        return words_with_max_char[0]
    else:
        return
