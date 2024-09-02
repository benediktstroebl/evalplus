
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    all_words = set()
    for word in words:
        all_words.add(word)
    max_len = len(sorted(all_words)[-1])
    max_len_words = list()
    for word in all_words:
        if len(word) == max_len:
            max_len_words.append(word)
    max_len_words = sorted(max_len_words)
    return max_len_words[0]

