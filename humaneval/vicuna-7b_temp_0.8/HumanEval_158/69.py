
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    n = len(words)
    max_char = 0
    max_word = ""
    for i in range(n):
        for j in range(i+1, n):
            if words[i] != words[j]:
                char_count = sum(ord(c) - ord('a') + 1 for c in words[i])
                char_count = char_count if char_count > max_char else max_char
                max_char = char_count
                max_word = words[i]
    return max_word
