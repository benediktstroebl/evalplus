
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    word_counts = {}
    for word in words:
        word = word.lower()
        if word not in word_counts:
            word_counts[word] = len(set(word))

    print(word_counts)

    return max(word_counts, key=word_counts.get)

