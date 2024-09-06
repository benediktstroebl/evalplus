
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def unique_chars(word):
        return len(set(word))

    def cmp_chars(word1, word2):
        return unique_chars(word1) - unique_chars(word2)

    def cmp_words(word1, word2):
        if unique_chars(word1) == unique_chars(word2):
            return cmp(word1, word2)
        return cmp_chars(word1, word2)

    return sorted(words, cmp=cmp_words)[-1]
