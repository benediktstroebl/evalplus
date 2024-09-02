
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    result = ""
    count = {}
    for word in words:
        unique_chars = set(word)
        if len(unique_chars) > len(count):
            count = unique_chars
        count_str = str(count)
        if count_str in words:
            word_count_str = words[count_str]
            if count_str[0] != word_count_str[0]:
                return count_str
        else:
            result = count_str
    return result
