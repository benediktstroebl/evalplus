
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # 1. Collect unique characters into a set
    # 2. Check if the set of the word is the biggest
    # 3. If so, return the word
    # 4. If not, go to the next one and repeat the process

    result = []
    max_chars = set()
    for word in words:
        char_set = set(word)
        if len(char_set) > len(max_chars):
            result = []
            result.append(word)
            max_chars = char_set
        elif len(char_set) == len(max_chars):
            result.append(word)

    return result[0]

