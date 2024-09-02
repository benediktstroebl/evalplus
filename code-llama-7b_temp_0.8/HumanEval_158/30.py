
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dic = {}
    for i in words:
        list_char = []
        list_char = list(i)
        for j in list_char:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
    max_num = 0
    max_word = ""
    for key in dic:
        if dic[key] > max_num:
            max_num = dic[key]
            max_word = key
    return max_word


