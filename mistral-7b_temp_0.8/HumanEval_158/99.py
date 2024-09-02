
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    from collections import defaultdict
    d = defaultdict(int)
    max_word = ''

    for word in words:
        for ch in word:
            d[ch] += 1

    for word in words:
        if sum(d[ch] for ch in word) == max(d.values()):
            if word < max_word:
                max_word = word
    return max_word


