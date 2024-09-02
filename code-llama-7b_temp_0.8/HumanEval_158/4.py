
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
        return ''

    max_string = words[0]
    max_unique_chars = len(set(words[0]))

    for word in words[1:]:
        if len(set(word)) > max_unique_chars:
            max_string = word
            max_unique_chars = len(set(word))
        elif len(set(word)) == max_unique_chars:
            if word < max_string:
                max_string = word

    return max_string
