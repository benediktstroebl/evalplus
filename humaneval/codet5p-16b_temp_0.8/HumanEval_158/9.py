
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    
    unique_chars = []
    for word in words:
        count = 0
        for char in set(word):
            count += word.count(char)
        unique_chars.append(count)

    max_unique_chars = max(unique_chars)
    return words[unique_chars.index(max_unique_chars)]

