
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    word_map = {}
    for word in words:
        if len(word) in word_map.keys():
            word_map[len(word)].append(word)
        else:
            word_map[len(word)] = [word]
    for word_length in word_map.keys():
        word_map[word_length].sort()
    result = word_map[max(word_map.keys())][0]
    for length, words in word_map.items():
        for word in words:
            if len(word) > len(result):
                result = word
    return result

