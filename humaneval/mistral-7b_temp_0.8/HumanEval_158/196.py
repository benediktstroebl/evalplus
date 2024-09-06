
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    if words == []:
        return None

    temp = []
    for word in words:
        set_word = set(word)
        count = len(set_word)
        temp.append([count, word])

    temp.sort(key = lambda x: x[0], reverse = True)
    max_word = ""
    for word in temp:
        if word[0] == temp[0][0]:
            max_word = word[1]

    return max_word


