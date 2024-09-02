
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # calculate unique characters
    # compare with others, return the first one
    # remove the first one
    # compare again, return the first one

    max_value = ''
    max_index = -1
    for i, word in enumerate(words):
        if word:
            char_count = {}
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1
            if len(char_count) > max_index or (len(char_count) == max_index and word < max_value):
                max_value = word
                max_index = len(char_count)
    return max_value

