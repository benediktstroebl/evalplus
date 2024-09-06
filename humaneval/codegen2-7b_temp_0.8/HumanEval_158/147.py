
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 0:
        return ""
    words = sorted(words)
    unique_chars = {}
    for word in words:
        for char in word:
            if char in unique_chars:
                unique_chars[char] += 1
            else:
                unique_chars[char] = 1
    if len(unique_chars.values()) == 1:
        return words[0]
    else:
        return max(unique_chars, key=unique_chars.get)

