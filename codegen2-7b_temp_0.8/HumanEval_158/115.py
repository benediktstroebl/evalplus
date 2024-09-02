
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    char_count = {}

    for word in words:
        for char in word:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

    max_count = max(char_count.values())

    for word in words:
        count = 0
        for char in word:
            if char_count[char] == max_count:
                count += 1
        if count == max_count:
            return word
    return ""

