
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
    maximum = 0
    position = 0
    dict_word = {}
    for i in range(len(words)):
        for j in words[i]:
            if j not in dict_word:
                dict_word[j] = 1
            else:
                dict_word[j] += 1
        if maximum < len(dict_word):
            maximum = len(dict_word)
            position = i
        dict_word = {}
    return words[position]

