
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    list = []
    for x in words:
        if list == []:
            list.append([x, len(set(x))])
        else:
            count = 0
            for i in range(len(list)):
                if list[i][1] < len(set(x)):
                    count += 1
                else:
                    break
            if count == len(list):
                list.append([x, len(set(x))])
            else:
                continue
    list.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return list[0][0]
    


