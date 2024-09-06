
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def helper(word):
        seen = set()
        for char in word:
            if char not in seen:
                seen.add(char)
            else:
                return 0
        return 1

    max_str = None
    max_helper = 0
    for word in words:
        if helper(word) > max_helper:
            max_helper = helper(word)
            max_str = word
    return max_str
