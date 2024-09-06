
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    longest_word = words[0]
    for word in words[1:]:
        if len(set(word)) > len(set(longest_word)):
            longest_word = word
        elif len(set(word)) == len(set(longest_word)) and word < longest_word:
            longest_word = word
    return longest_word
