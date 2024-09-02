
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
        for letter in word:
            if letter in word_count:
                word_count[letter] += 1
            else:
                word_count[letter] = 1

    word_count = sorted(word_count, key=word_count.get, reverse=True)
    if word_count:
        return word_count[0]
    return ""
