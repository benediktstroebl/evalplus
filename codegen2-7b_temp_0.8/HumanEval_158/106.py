
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dict_words = {}
    for word in words:
        key_word = ""
        for word_ch in word:
            if word_ch not in dict_words:
                dict_words[word_ch] = 1
            else:
                dict_words[word_ch] += 1
        dict_words = {k: v for k, v in sorted(dict_words.items(), key=lambda item: item[1], reverse=True)}
    return [word for word, count in dict_words.items() if count == max(dict_words.values
