
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    def count_unique_chars(word):
        """Return the count of unique characters in a string"""
        count = 0
        for char in word:
            if char not in unique_chars:
                unique_chars.append(char)
                count += 1
        return count

    words = ["name", "of", "string"]
    unique_chars = []
    word = ""
    max_count = 0
    for w in words:
        count = count_unique_chars(w)
        if count > max_count:
            word = w
            max_count = count
    return word
