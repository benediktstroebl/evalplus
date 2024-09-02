
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
        return ""

    max_word = words[0]
    max_set = set(max_word)

    for word in words[1:]:
        current_set = set(word)
        if len(current_set) > len(max_set):
            max_set = current_set
            max_word = word

        elif len(current_set) == len(max_set):
            if word < max_word:
                max_word = word

    return max_word
