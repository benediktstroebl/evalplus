
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    def unique(w1, w2):
        return len(set(w1)) > len(set(w2))

    def max(words):
        max = words[0]
        for word in words:
            if unique(max, word):
                max = word
        return max

    words.sort()
    return max(words)
