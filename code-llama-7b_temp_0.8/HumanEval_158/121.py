
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    uniq_count = 0
    uniq_max = 0
    word_max = ""

    for word in words:
        uniq_count = 0
        for letter in word:
            if word.count(letter) == 1:
                uniq_count += 1
        if uniq_count > uniq_max:
            uniq_max = uniq_count
            word_max = word
    return word_max
