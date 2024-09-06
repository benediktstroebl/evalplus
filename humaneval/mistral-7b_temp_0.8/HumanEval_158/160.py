
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    import string
    from collections import Counter

    max_value = ""
    for word in words:
        # convert to lowercase for lexicographical order
        word = word.lower()
        c = Counter(word)
        if max_value == "":
            # first word in lexicographical order
            max_value = word
        else:
            # compares all words with max_value
            if c == Counter(max_value):
                if word < max_value:
                    max_value = word

    return max_value
