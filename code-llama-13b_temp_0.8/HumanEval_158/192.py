
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def unique(string):
        string = sorted(string)
        string = ''.join(string)
        return len(string) == len(set(string))

    def count_unique(string):
        return len(set(string))
    
    # if not any(words):
    #     return ""
    result = [word for word in words if unique(word)]

    if not result:
        return ""

    result = sorted(result, key=count_unique)
    return sorted(result, key=lambda x:x[0])[-1]


