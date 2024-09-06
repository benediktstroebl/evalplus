
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = {}
    max_chars[0] = {0: True}
    for word in words:
        temp = {}
        for i in range(len(word)):
            if i not in max_chars:
                temp[i] = True
                continue
            temp[i] = True if word[i] not in max_chars[i] else False
        max_chars[len(word)] = temp
    for i in range(len(words)):
        if len(max_chars[i]) == len(words[i]):
            return words[i]
    return ""

