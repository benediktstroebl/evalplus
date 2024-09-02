
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    char_map = {}
    for word in words:
        for char in word:
            if char not in char_map:
                char_map[char] = 0
            char_map[char] += 1
    
    max_word = ""
    for word in words:
        if max_word == "":
            max_word = word
        elif max_word < word:
            max_word = word
        elif max_word > word:
            continue
        else:
            if len(word) < len(max_word):
                max_word = word
    return max_word
