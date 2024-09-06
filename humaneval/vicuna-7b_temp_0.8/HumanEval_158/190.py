
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def count_chars(word):
        """Count the number of unique characters in a word"""
        char_count = {}
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count

    max_word = max(words, key=count_chars)
    return max_word
