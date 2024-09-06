
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    result = ""  # this will store the word with the maximum number of unique characters
    max_count = 0  # this will store the number of unique characters of the word with the maximum number of unique characters
    for word in words:
        unique_count = 0
        for char in word:
            if char not in result:
                unique_count += 1
        if unique_count > max_count:
            max_count = unique_count
            result = word
    return result

