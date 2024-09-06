
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_unique = 0
    max_unique_word = None

    for word in words:
        unique_count = 0

        for char in word:
            if char in word.replace(char, ''):
                unique_count += 1

        if unique_count >= max_unique:
            max_unique = unique_count
            max_unique_word = word

    return max_unique_word
