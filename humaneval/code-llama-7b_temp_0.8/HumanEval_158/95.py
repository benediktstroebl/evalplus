
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

    first_max = words[0]
    count_max = len(set(first_max))

    for i in range(1, len(words)):
        if len(set(words[i])) > count_max:
            first_max = words[i]
            count_max = len(set(words[i]))
        elif len(set(words[i])) == count_max:
            if words[i] < first_max:
                first_max = words[i]

    return first_max

