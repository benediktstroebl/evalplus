
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    dic_words = {}
    for word in words:
        # Generate a dictionary with the word and it's unique characters.
        dic_words[word] = set(word)

    # Find the max length of the unique chars.
    max_length = max(len(unique) for unique in dic_words.values())
    # Generate a list of the words with the max length of unique characters.
    max_words = [k for k, v in dic_words.items() if len(v) == max_length]
    # Return the first word in the list.
    return max_words[0]

