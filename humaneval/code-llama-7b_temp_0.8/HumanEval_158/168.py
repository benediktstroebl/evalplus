
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Hash maps
    # Sort
    # find longest string with the same number of unique characters as the
    # shortest string
    # return the shortest string

    # Hash map implementation
    letter_count = {}
    for word in words:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    longest_string_len = 0
    longest_string = ""
    shortest_string_len = 0
    shortest_string = ""

    for word in words:
        word_len = len(word)
        if word_len > longest_string_len:
            longest_string_len = word_len
            longest_string = word

        if word_len < shortest_string_len:
            shortest_string_len = word_len
            shortest_string = word

    count = 0
    for letter in shortest_string:
        if letter in letter_count:
            count += 1

    if count == longest_string_len:
        return shortest_string
    else:
        return longest_string
