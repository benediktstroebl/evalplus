
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word_dict = {}
    for word in words:
        letters = set(word)
        word_dict[word] = len(letters)
    word_dict = dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))
    # print(word_dict)
    first_max_word = list(word_dict.keys())[0]
    for key in word_dict:
        if word_dict[key] == word_dict[first_max_word]:
            if key < first_max_word:
                first_max_word = key
    return first_max_word

