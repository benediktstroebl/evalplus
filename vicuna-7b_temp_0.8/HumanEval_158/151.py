
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word_count = max([len(word) for word in words])
    max_word = ""
    for word in words:
        count = {}
        for c in word:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        word_count = len(count)
        if word_count > max_word_count:
            max_word = word
            max_word_count = word_count
    return max_word