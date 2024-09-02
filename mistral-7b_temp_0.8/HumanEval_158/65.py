
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    sorted_list = sorted(words, key=len, reverse=True)
    current_max = 0
    max_str = ""
    for w in sorted_list:
        uniq_chars = set()
        for c in w:
            uniq_chars.add(c)
        if len(uniq_chars) > current_max:
            current_max = len(uniq_chars)
            max_str = w

    return max_str

