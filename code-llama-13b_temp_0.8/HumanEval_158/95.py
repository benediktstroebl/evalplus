
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
        return 0
    
    max_word = words[0]

    for word in words:
        unique_characters = 0
        for char in word:
            if char in set(max_word):
                continue
            else:
                unique_characters += 1

        if unique_characters >= len(max_word):
            max_word = word

    return max_word

