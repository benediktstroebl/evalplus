
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # your code here
    max_str = ""
    max_count = 0
    for word in words:
        unique_char = set(word)
        if len(unique_char) > max_count:
            max_count = len(unique_char)
            max_str = word
        elif len(unique_char) == max_count:
            if word < max_str:
                max_str = word

    return max_str
