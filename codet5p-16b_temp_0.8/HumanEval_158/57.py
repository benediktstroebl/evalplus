
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    unique_words = []
    unique_letters = set()
    for word in words:
        for letter in word:
            unique_letters.add(letter)
        unique_words.append(len(unique_letters))
    return words[unique_words.index(max(unique_words))]
