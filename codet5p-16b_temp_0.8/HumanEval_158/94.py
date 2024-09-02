
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    unique_characters = []
    unique_counts = []
    for word in words:
        count = len(set(word))
        unique_counts.append(count)
        unique_characters.append(word)
    index = unique_counts.index(max(unique_counts))
    return unique_characters[index]

