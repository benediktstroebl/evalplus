
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    
    words.sort()
    max_words = list()
    max_unique = 0
    for i in words:
        if len(set(i)) > max_unique:
            max_unique = len(set(i))
            max_words = [i]
        elif len(set(i)) == max_unique:
            max_words.append(i)
    return min(max_words)

    
    
    

