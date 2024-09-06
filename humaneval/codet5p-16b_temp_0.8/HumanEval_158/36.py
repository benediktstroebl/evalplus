
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    for word in words:
        if len(words) == 0:
            return ""
        else:
            if len(words) == 1:
                return words[0]
            else:
                count = 0
                for i in range(len(words)):
                    if len(words[i]) > count:
                        count = len(words[i])
                        max_index = i
                max_index = words[i]
    return max_index

