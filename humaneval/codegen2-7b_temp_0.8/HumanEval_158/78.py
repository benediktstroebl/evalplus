
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    """
    time: O(n * m), n = len(words) and m = len(set(words))
    space: O(n + m)
    """
    def find_word(word):
        return word.split()
    sorted_words = sorted(words, key=lambda word: len(set(word)))
    return sorted_words[-1] if sorted_words else ''


