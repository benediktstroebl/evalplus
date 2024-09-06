
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_num = 0
    max_word = None
    for word in words:
        word_dict = {}
        for letter in word:
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1

        if len(word_dict) > max_num:
            max_word = word
            max_num = len(word_dict)

    return max_word

