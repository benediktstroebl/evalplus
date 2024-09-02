
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 0:
        return None
    if len(words) == 1:
        return words[0]
    
    def compare(a,b):
        if a == b:
            return 0
        elif a > b:
            return 1
        else:
            return -1

    max_string = words[0]
    max_unique = len(max_string)
    for word in words[1:]:
        if len(word) > max_unique:
            max_string = word
            max_unique = len(word)
        elif len(word) == max_unique:
            if compare(word, max_string) == -1:
                max_string = word

    return max_string

