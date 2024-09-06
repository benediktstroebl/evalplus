
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
    max_word = None
    for word in words:
        if len(word) == 1:
            continue
        for char in word:
            if char.isalpha():
                if char.lower() not in word_count:
                    word_count[char.lower()] = word_count.get(char.lower(), 0) + 1
        if word_count:
            if max_word is None or word_count[word.lower()] > max_word_count:
                max_word = word.lower()
                max_word_count = word_count[max_word]
    return max_word
