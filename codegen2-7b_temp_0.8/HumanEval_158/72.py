
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words_count = {}
    for word in words:
        for char in word:
            if char in words_count:
                words_count[char] += 1
            else:
                words_count[char] = 1

    max_count = max(words_count.values())

    for word in words:
        if words_count[word] == max_count:
            return word

    
