
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words = list(words)
    max_words = []
    for word in words:
        char_count = dict()
        for c in word:
            if c not in char_count:
                char_count[c] = 1
            else:
                char_count[c] += 1
        if len(char_count) > len(max_words):
            max_words = [word]
        elif len(char_count) == len(max_words):
            max_words.append(word)

    if len(max_words) == 1:
        return max_words[0]
    else:
        return min(max_words)
