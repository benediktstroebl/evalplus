
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def max_unique(word):
        return len(set(word))

    word_list = [(w, max_unique(w)) for w in words]
    max_count = max([t[1] for t in word_list])
    return [t[0] for t in word_list if t[1] == max_count][0]
