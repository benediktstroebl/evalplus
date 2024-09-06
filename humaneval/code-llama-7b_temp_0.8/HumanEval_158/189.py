
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    char_list = []
    for word in words:
        char_list.append(set(word))

    word_count = {}
    for word, char_set in zip(words, char_list):
        word_count[word] = len(char_set)
    max_char_count = max(word_count.values())

    max_words = []
    for word, char_set in zip(words, char_list):
        if word_count[word] == max_char_count:
            max_words.append(word)

    return min(max_words)

