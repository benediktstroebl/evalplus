
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
    unique_char = {0:0}
    for word in words:
        word = set(word)
        if len(word) not in unique_char.keys():
            unique_char[len(word)] = word
        else:
            unique_char[len(word)] = min(word,unique_char[len(word)])

    return min(unique_char.values())
