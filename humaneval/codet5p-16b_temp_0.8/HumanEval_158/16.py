
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    if len(words) == 1:
        return words[0]
    else:
        unique_words = []
        for word in words:
            unique_words.append(set(word))
        common_characters = []
        for word in unique_words:
            common_characters.append(len(word))
        maximum = max(common_characters)
        for word in words:
            if len(word) == maximum:
                return word




