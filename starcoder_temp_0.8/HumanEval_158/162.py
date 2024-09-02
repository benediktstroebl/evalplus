
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
        return ""
    count = 0
    s1 = words[0]
    for i in range(len(s1)):
        for j in range(len(words)):
            if s1[i] in words[j]:
                count += 1
        if count == 1:
            return s1
        count = 0
        s1 = s1[1:]
    return ""
