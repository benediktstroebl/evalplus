
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    #print("find_max: ", words)

    max_characters = 0
    max_string = ""
    for string in words:
        if len(string) == max_characters:
            max_string = string if string < max_string else max_string
        elif len(string) > max_characters:
            max_string = string
            max_characters = len(string)

    return max_string

