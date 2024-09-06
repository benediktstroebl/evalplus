
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def get_max_unique(words):
        """Return the word with maximum number of unique characters."""
        if len(words) == 0:
            return ""
        else:
            most_unique = 0
            for word in words:
                if len(word) > most_unique:
                    most_unique = len(set(word))
            return most_unique

    max_unique = get_max_unique(words)
    for word in words:
        if len(word) == max_unique:
            return word
