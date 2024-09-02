
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    if not words:
        return None

    chars_set = set()
    max_count = 0
    max_word = ""

    for word in words:
        chars_set.clear()

        for letter in word:
            if letter not in chars_set:
                chars_set.add(letter)

        if len(chars_set) > max_count:
            max_count = len(chars_set)
            max_word = word

    return max_word

