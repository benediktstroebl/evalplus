
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    unique_count = {}

    for word in words:
        for char in word:
            unique_count[char] = word.count(char)
    max_count = max(unique_count.values())

    for word in words:
        if max_count == unique_count[word[0]]:
            return word
