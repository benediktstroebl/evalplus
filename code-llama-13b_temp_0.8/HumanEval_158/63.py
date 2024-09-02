
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = 0
    max_word = ""
    dict = {}
    for word in words:
        uniq = 0
        for char in word:
            if char not in dict:
                dict[char] = char
                uniq += 1
        if uniq > max_len:
            max_len = uniq
            max_word = word
    return max_word

