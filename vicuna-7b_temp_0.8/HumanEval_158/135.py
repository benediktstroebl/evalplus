
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = max([len(word) for word in words])
    max_word = ""
    for word in words:
        for i in range(len(word)):
            if word[i] in "aeiouAEIOU":
                max_word += word[i]
            elif word[i] in "bcdfghjklmnpqrstvwxyz":
                max_word += word[i].upper()
            else:
                max_word += word[i]
        max_len = max(max_len, len(max_word))
    return max_word