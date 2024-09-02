
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word_count = {}
    max_word = ""
    for word in words:
        count = 0
        for char in word:
            if char in word_count:
                count = word_count[char]
            else:
                word_count[char] = 1
                count = 1
        max_word = word if count == len(word) else max_word
    return max_word