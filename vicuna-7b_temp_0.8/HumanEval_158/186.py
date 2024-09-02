
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = max(len(word) for word in words)
    max_word = "".join(words)
    if len(set(max_word)) == max_chars:
        return max_word
    else:
        for i in range(1, len(max_word)):
            for j in range(i, len(max_word)):
                word = max_word[:i] + max_word[j] + max_word[i+1:]
                if len(set(word)) == max_chars:
                    return word
    return max_word