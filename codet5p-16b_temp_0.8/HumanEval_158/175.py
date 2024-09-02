
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    words = [word.lower() for word in words]
    words = sorted(words, key=len)
    max_len = len(words[0])
    max_unique = [word for word in words if len(set(word)) == max_len]
    return min(max_unique, key=lambda x: words.index(x))
    
