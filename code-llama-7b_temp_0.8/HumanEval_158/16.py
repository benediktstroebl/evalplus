
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Without using Counter.
    pass

    # Using Counter.
    from collections import Counter

    max_unique_count = 0
    result = ''

    for word in words:
        count = len(Counter(word).keys())
        if count > max_unique_count:
            max_unique_count = count
            result = word
        elif count == max_unique_count and word < result:
            result = word

    return result
