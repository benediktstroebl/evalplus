
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    my_dict = {}
    my_list = []
    for i in words:
        my_dict[i] = len(set(i))
    for k in my_dict.keys():
        if my_dict[k] == max(my_dict.values()):
            my_list.append(k)
    my_list = sorted(my_list)
    return my_list[0]



