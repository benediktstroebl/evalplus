
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
    max_chars = max([len(word) for word in words])
    max_word = ""
    max_char = 0
    for i in range(n):
        for j in range(i+1, n):
            if words[i].count(words[j]) == max_chars:
                max_chars -= words[j].count(words[i])
                max_char = max_char + words[j].count(words[i])
                if max_char > max_chars:
                    max_chars = max_char
                    max_word = words[i]
    return max_word
