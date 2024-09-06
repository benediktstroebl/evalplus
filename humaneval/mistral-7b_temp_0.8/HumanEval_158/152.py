
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word = words[0]
    max_length = 0
    for w in words:
        count = {}
        for letter in w:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1
        if len(count) > max_length:
            word = w
            max_length = len(count)
    return word

