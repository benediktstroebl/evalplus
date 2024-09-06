
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # if len(words) == 0:
    #     return "None"

    # max_str = ""
    # for s in words:
    #     char_set = set()
    #     for c in s:
    #         if c in char_set:
    #             pass
    #         else:
    #             char_set.add(c)
    #     if len(char_set) > len(max_str):
    #         max_str = s
    # return max_str

    # 2nd solution: O(n) time | O(n) space
    max_length = 0
    max_word = ""
    for word in words:
        length = 0
        for char in word:
            if char not in max_word:
                length += 1
        if length > max_length:
            max_length = length
            max_word = word
    return max_word




