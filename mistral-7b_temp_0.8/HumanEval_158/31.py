
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

    def is_unique(word):
        char_count = [0] * 256
        for char in word:
            char_count[ord(char)] += 1
            if char_count[ord(char)] > 1:
                return False
        return True

    max_word = ""
    for word in words:
        if is_unique(word) and len(word) > len(max_word):
            max_word = word
    return max_word

