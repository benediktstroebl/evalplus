
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # sort the list of words so that words with more unique characters come first
    words = sorted(words, key=len, reverse=True)
    # find the index of the first non-repeating character
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] == words[j]:
                break
        else:
            return words[i]
    return words[0]
