
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_chars = 0
    result = ""
    for word in words:
        current_chars = 0
        for letter in word:
            if word.count(letter) == 1:
                current_chars += 1
        if current_chars > max_chars:
            max_chars = current_chars
            result = word
    return result
