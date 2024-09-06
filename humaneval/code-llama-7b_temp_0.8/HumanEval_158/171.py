
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # s = set(words[0])
    # for word in words:
    #     for letter in word:
    #         if letter not in s:
    #             s.add(letter)
    #         else:
    #             continue
    #     if len(s) > len(words[0]):
    #         s = set(word)
    # return word
    return max(words, key=lambda w: (len(set(w)), w))

