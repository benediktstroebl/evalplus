
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_count = 0
    max_word = None
    for word in words:
        count = 0
        for i in range(0, len(word)):
            if word.count(word[i]) > count:
                count = word.count(word[i])
        if count > max_count:
            max_word = word
            max_count = count
    return max_
