
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
        return ""
    if len(words) == 1:
        return words[0]

    # put all unique characters in a set
    set1 = set()
    for word in words:
        for c in word:
            if c not in set1:
                set1.add(c)

    # find word with maximum number of unique characters
    max_num = 0
    max_word = ""
    for word in words:
        count = len(set(word))
        if count > max_num:
            max_num = count
            max_word = word
    return max_word

