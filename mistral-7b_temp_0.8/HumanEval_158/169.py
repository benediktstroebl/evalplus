
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_string = ""
    max_num = 0
    for string in words:
        num_of_unique_chars = 0
        for char in string:
            if char not in string[0:string.index(char)]:
                num_of_unique_chars += 1
        if num_of_unique_chars > max_num:
            max_num = num_of_unique_chars
            max_string = string
    return max_string

