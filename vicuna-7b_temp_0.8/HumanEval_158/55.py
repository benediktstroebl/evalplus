
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = max(len(word) for word in words)
    max_word = ""
    for word in words:
        count = 0
        for c in word:
            if c not in count:
                count += 1
        if count == 0:
            count = 1
        else:
            count -= 1
        if len(word) == max_len and word.lower() == " ".join(sorted(words)).lower():
            max_word = word
    return max_word
