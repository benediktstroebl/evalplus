
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    sorted_words = sorted(words)
    unique_chars = []
    max_unique_chars = 0
    for word in sorted_words:
        if not unique_chars:
            unique_chars.append(word)
        else:
            if unique_chars[-1] == word:
                unique_chars.append(word)
            else:
                unique_chars.append(word)
                unique_chars = sorted(unique_chars)
                if len(unique_chars[-1]) > max_unique_chars:
                    max_unique_chars = len(unique_chars[-1])
                    result = unique_chars[-1]
    return result

