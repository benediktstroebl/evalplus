
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""
    max_words = max(words, key=len, keepattr=True)
    max_word = max_words[0]
    max_chars = len(max_word)
    for word in words[1:]:
        word_chars = len(word)
        if max_chars == word_chars:
            if max_word[0] > word[0]:
                max_word = word
                max_chars = len(max_word)
        elif max_chars > word_chars:
            max_word = word
            max_chars = len(max_word)
    return max_word
