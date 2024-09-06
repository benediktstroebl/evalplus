
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 0:
        return ""
    if len(words) == 1:
        return words[0]
    result = words[0]
    counter = {}
    for word in words:
        for ch in word:
            if ch not in counter:
                counter[ch] = 1
            else:
                counter[ch] += 1
    for word in words:
        if len(word) == len(set(word)):
            if result < word:
                result = word
    return
