
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word_length_dict = {}
    max_word = ""
    for word in words:
        if len(set(word)) not in word_length_dict:
            word_length_dict[len(set(word))] = []
        word_length_dict[len(set(word))].append(word)
    for length, words in word_length_dict.items():
        words.sort()
        max_word = words[0]
    return max_word

