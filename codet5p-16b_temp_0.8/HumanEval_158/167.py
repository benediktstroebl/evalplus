
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
        return None
    unique_words = set()
    for word in words:
        unique_words.add(word)
    max_unique_characters = len(unique_words)
    max_unique_word = ""
    for word in words:
        if len(unique_words) > max_unique_characters:
            max_unique_word = word
            max_unique_characters = len(unique_words)
            unique_words = set()
            unique_words.add(word)
        elif len(unique_words) == max_unique_characters:
            max_unique_word = min(max_unique_word, word)
            unique_words.add(word)
    return max_unique_word
