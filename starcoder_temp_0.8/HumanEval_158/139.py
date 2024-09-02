
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_string = words[0]
    max_count = find_unique(words[0])
    for i in range(1, len(words)):
        count = find_unique(words[i])
        if count > max_count:
            max_count = count
            max_string = words[i]
        elif count == max_count:
            max_string = min(max_string, words[i])
    return max_string

