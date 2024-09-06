
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
        unique_chars.append(len(set(word)))
    max_count = max(unique_chars)
    result = []
    for i in range(len(unique_chars)):
        if unique_chars[i] == max_count:
            result.append(words[i])
    return sorted(result)[0]

