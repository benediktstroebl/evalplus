
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
            if char.isalpha():
                if char.lower() not in unique_chars:
                    unique_chars[char.lower()] = 1
                    max_chars = max(word)
    return words[unique_chars.most_common(max_chars)[0][0]]
