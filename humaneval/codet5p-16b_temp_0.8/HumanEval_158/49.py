
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    new_words = []
    for i in words:
        new_words.append(i.lower())
    new_words.sort()
    new_words.reverse()
    print(new_words)
    new_word = new_words[0]
    for i in range(1, len(new_words)):
        if len(new_words[i]) > len(new_word):
            new_word = new_words[i]
    return new_word

