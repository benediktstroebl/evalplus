
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    longest = ""
    current_longest = ""
    for word in words:
        if len(longest) == len(word):
            if word > longest:
                current_longest = word
        if len(longest) < len(word):
            current_longest = word
            longest = word
    return current_longest

