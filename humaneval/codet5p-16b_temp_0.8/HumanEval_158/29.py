
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_chars = []
    words_dict = {}
    for word in words:
        chars = []
        for char in word:
            chars.append(char)
        words_dict[word] = set(chars)
    for word in words:
        if words_dict[word] == set(words_dict[word]):
            if words_dict[word] > set(max_chars):
                max_chars = list(words_dict[word])
                max_word = word
    if max_word == None:
        return ""
    return max_word
