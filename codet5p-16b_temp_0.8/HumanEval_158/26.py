
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    count = 0
    unique = 0
    result = ""
    for word in words:
        for character in word:
            if character not in word:
                count += 1
        if count > unique:
            unique = count
            result = word
        count = 0
    return result
