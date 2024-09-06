
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    def find_unique(word):
        chars = set()
        for char in word:
            chars.add(char)
        return len(chars)

    max_word = ""
    max_unique = 0
    for word in words:
        word_unique = find_unique(word)
        if word_unique > max_unique:
            max_word = word
            max_unique = word_unique
        elif word_unique == max_unique:
            if word < max_word:
                max_word = word
    return max_word

