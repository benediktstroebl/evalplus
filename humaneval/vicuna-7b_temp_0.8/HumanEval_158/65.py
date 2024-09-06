
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word = ""
    max_chars = {}
    for word in words:
        if len(word) == 0:
            continue
        ch = word[0]
        if ch in max_chars:
            max_chars[ch] += 1
        else:
            max_chars[ch] = 1
    for word in words:
        if len(word) == 0:
            continue
        for char in word:
            if char not in max_chars:
                max_chars[char] = 1
        max_word = max(max_word, word)
    return max_word

test = ["name", "of", "string"]
