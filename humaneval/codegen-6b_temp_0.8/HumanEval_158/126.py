
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_chars = {}
    for word in words:
        for char in word:
            if char not in unique_chars:
                unique_chars[char] = 1
            else:
                unique_chars[char] += 1

    max_word = sorted(words, key=lambda x: len(x))[-1]
    max_count = len(unique_chars)
    for word in unique_chars:
        if unique_chars[word] > max_count:
            max_count = unique_chars[word]
            max_word = word

    return max_word

