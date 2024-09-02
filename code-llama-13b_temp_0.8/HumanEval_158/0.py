
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_chars = {}
    for word in words:
        unique_chars[word] = len(set(word))
    print(unique_chars)
    max_unique_chars = max(unique_chars.values())
    max_unique_words = []
    for key, value in unique_chars.items():
        if value == max_unique_chars:
            max_unique_words.append(key)
    return sorted(max_unique_words)[0]




