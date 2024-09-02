
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
        if len(word) not in word_dict:
            word_dict[len(word)] = word
        elif word not in word_dict:
            word_dict[word] = word
        else:
            word_dict[word] = ""

    word_list = []
    for word, count in word_dict.items():
        if count == "":
            word_list.append(word)

    return "".join(word_list) if word_list else
