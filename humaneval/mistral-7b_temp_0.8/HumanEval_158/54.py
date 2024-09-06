
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_string = ''
    for string in words:
        counter = 0
        for i in range(len(string)):
            for j in range(i + 1, len(string)):
                if string[i] == string[j]:
                    counter += 1
        if counter < len(string):
            max_string = string
    return max_string

