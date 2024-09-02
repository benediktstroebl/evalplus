
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
    for word in words:
        for char in word:
            if char in word_count:
                word_count[char] += 1
            else:
                word_count[word] = 1
    max_word = max(word_count, key=word_count.get)
    return max_word
