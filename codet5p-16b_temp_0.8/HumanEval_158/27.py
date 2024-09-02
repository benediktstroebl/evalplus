
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_count = 0
    result = ""
    for i in words:
        count = 0
        for j in i:
            if i.count(j) == 1:
                count += 1
        if count > max_count:
            max_count = count
            result = i
    return result
