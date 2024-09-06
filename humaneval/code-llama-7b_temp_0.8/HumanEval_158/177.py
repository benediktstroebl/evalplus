
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if words == None:
        return None

    if len(words) < 2:
        return None

    hash_map = {}
    max_count = 0
    index = 0

    for word in words:
        hash_map[word] = []
        for char in word:
            if char not in hash_map[word]:
                hash_map[word].append(char)

        if len(hash_map[word]) > max_count:
            max_count = len(hash_map[word])
            index = words.index(word)

    return words[index]
