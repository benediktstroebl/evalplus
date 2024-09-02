
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    longest, max_char = "", -1
    for word in words:
        counter = set()
        for char in word:
            if char not in counter:
                counter.add(char)
            if len(counter) > max_char:
                longest, max_char = word, len(counter)
    return longest
