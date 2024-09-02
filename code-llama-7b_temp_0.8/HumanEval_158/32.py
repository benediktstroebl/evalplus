
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words_length = []
    unique_char_count = []
    for word in words:
        words_length.append(len(word))
        unique_char_count.append(len(set(word)))
    max_length = max(words_length)
    max_unique_char = max(unique_char_count)
    max_index = words_length.index(max_length)
    if unique_char_count[max_index] == max_unique_char:
        return words[max_index]
    else:
        for word in words:
            if len(word) == max_length:
                if len(set(word)) == max_unique_char:
                    return word

