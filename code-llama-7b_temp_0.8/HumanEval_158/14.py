
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
        return ""
    if len(words) == 1:
        return words[0]

    if len(words) == 2:
        if len(words[0]) > len(words[1]):
            return words[0]
        elif len(words[0]) < len(words[1]):
            return words[1]
        else:
            if words[0] < words[1]:
                return words[1]
            else:
                return words[0]

    max_str = words[0]
    max_num = get_num_of_unique_chars(max_str)
    for word in words:
        unique_chars_num = get_num_of_unique_chars(word)
        if unique_chars_num >= max_num:
            max_num = unique_chars_num
            max_str = word
    return max_str

