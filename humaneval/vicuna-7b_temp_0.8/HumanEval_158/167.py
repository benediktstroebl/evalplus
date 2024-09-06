
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words_count = {}
    max_word = ""
    for word in words:
        if len(set(word)) <= len(word):
            word = word.lower()
            for char in word:
                if char.isalnum() and word.count(char) > words_count[char]:
                    max_word = word
                    words_count[char] = word.count(char)
    return max_word
