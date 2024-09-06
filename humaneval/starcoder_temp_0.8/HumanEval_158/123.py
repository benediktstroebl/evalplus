
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    counts = []
    for word in words:
        counts.append(len(set(word)))
    counts_indexes = [i for i in range(len(counts))]

    counts, counts_indexes = zip(*sorted(zip(counts, counts_indexes), reverse = True))
    return words[counts_indexes[0]]
