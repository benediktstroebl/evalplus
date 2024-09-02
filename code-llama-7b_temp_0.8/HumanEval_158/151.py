
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    max_word = ""
    max_word_size = 0
    word_dict = {}

    for word in words:
        if len(word) > max_word_size:
            max_word = word
            max_word_size = len(word)
        if len(word) == max_word_size:
            if word not in word_dict.keys():
                word_dict[word] = True
            elif word_dict[word]:
                max_word = word
                word_dict[word] = False
    return max_word
