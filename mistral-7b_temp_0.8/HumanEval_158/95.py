
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if words == []:
        return None

    word_max = words[0]
    for word in words:
        if len(word) > len(word_max):
            word_max = word
        elif len(word) == len(word_max):
            if word < word_max:
                word_max = word
    return word_max
