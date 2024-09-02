
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    counts = {}
    for word in words:
        counts[word] = len(set(word))

    # return max(counts, key=counts.get)

    max_word = None
    max_val = None
    for w, v in counts.items():
        if max_val is None or max_val < v:
            max_word, max_val = w, v
        elif max_val == v:
            if w < max_word:
                max_word, max_val = w, v

    return max_word

