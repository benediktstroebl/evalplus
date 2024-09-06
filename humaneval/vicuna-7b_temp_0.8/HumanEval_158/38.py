
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = {}
    max_len = 0
    for word in words:
        char_count = 0
        for char in word:
            if char in max_chars:
                char_count -= max_chars[char]
            else:
                max_chars[word] = 1
                char_count += 1
        max_len = max(max_len, len(word))
        if max_chars[word] > max_chars[next_max]:
            max_chars[next_max], max_chars[word] = max_chars[word], max_chars[next_max]
            if max_len == len(next_max):
                max_len = max(max_len, len(word))
    return next_max

next_max = find_max(words)
