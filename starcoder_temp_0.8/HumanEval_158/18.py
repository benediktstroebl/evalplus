
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    new = []

    for i in range(len(words)):
        temp = []
        for j in range(len(words[i])):
            if words[i][j] not in temp:
                temp.append(words[i][j])
        new.append(temp)

    unique = [len(i) for i in new]
    max_val = max(unique)

    for i in range(len(unique)):
        if unique[i] == max_val:
            return words[i]
