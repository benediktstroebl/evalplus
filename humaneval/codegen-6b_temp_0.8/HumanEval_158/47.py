
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = {}
    for word in words:
        if len(word) not in max_len:
            max_len[len(word)] = 1
        else:
            max_len[len(word)]+=1

    max_len_char = max_len[max(max_len)]
    max_len_words = [i for i in words if max_len_char == len(i)]
    return sorted(max_len_words)[0]

