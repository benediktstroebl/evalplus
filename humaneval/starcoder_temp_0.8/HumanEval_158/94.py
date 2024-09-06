
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    counter = {}
    max_ = 0
    string_with_max = None
    for string in words:
        counter = get_unique_chars(string)
        if len(counter.keys()) > max_:
            max_ = len(counter.keys())
            string_with_max = string
        elif len(counter.keys()) == max_:
            if string < string_with_max:
                string_with_max = string
    return string_with_max

