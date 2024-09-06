
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    char_set = set()
    temp_max = 0
    max_char = ""
    for word in words:
        if len(word) > temp_max:
            max_char = word
            temp_max = len(word)
        elif len(word) == temp_max:
            if word < max_char:
                max_char = word
        temp = ""
        for char in word:
            if char not in temp:
                temp += char
        char_set = char_set.union(temp)

    return max_char
