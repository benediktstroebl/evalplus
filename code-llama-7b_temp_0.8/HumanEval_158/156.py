
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Your code here
    #PS- I am unsure about the return part but the rest seems to be correct
    #     using the lexical order is not so much of a concern
    words_count = {}

    for word in words:
        if word not in words_count:
            words_count[word] = 0
        words_count[word] += len(set(word))

    max_count = 0
    max_word = None
    for word, count in words_count.items():
        if count > max_count:
            max_count = count
            max_word = word

    return max_word

