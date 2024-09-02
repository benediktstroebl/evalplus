
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
        raise ValueError("Words must be provided.")
    if len(words) == 1:
        return words[0]

    word_count = {}
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) not in word_count:
            word_count[len(unique_chars)] = []
        word_count[len(unique_chars)].append(word)
    max_word = max(word_count, key=lambda key: len(word_count[key]))
    return max(word_count[max_word], key=lambda word: sorted(word))
