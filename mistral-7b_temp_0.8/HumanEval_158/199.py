
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
        unique_chars_dict = {}
        for char in word:
            if char not in unique_chars_dict:
                unique_chars_dict[char] = 1
            else:
                unique_chars_dict[char] += 1
        return len(unique_chars_dict)
    max_unique_chars = 0
    max_unique_chars_word = ""
    for word in words:
        if count_unique_chars(word) > max_unique_chars:
            max_unique_chars = count_unique_chars(word)
            max_unique_chars_word = word
    return max_unique_chars_word
