
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # 1
    # for string in words:
    #     for character in string:
    #         if character not in string:
    #             break
    #         else:
    #             return string
    # return ""

    # 2
    # for string in words:
    #     result = set(string)
    #     if len(result) == len(string):
    #         return string
    # return ""

    # 3
    longest = ""
    for string in words:
        unique_chars = set(string)
        if len(unique_chars) == len(string) and len(unique_chars) > len(longest):
            longest = string

    return longest

