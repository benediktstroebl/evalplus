
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # May be a little bit of overhead, but let's make it correct first :)
    unique_chars = {}
    for word in words:
        for char in word:
            if char not in unique_chars:
                unique_chars[char] = 1
            else:
                unique_chars[char] += 1

    result = ""
    max_chars = 0
    for key, value in unique_chars.items():
        if max_chars < value:
            max_chars = value
            result = key
        elif max_chars == value:
            if key < result:
                result = key
    return result

