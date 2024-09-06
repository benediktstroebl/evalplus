
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # count the number of unique characters in each string
    char_count = {}
    for word in words:
        for char in word:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

    # sort the words by the number of unique characters
    words.sort(key=lambda x: char_count[x])

    # return the word with maximum number of unique characters
    return words[0] if words else ""
