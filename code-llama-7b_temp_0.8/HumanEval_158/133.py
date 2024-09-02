
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
    for w in words:
        if len(set(w)) > len(set(longest)):
            longest = w
        elif len(set(w)) == len(set(longest)) and w < longest:
            longest = w
    return longest


