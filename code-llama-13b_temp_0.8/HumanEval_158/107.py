
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def count_unique(string):
        string = string.lower()
        chars = {}
        for i in string:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1
        return len(chars)
    
    return max(words, key=count_unique)
