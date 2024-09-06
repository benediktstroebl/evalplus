
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    def get_count(word):
        return len(set(word))

    def get_lex_order(word1, word2):
        if word1 < word2:
            return word1
        else:
            return word2

    if len(words) == 0:
        return ""

    return max(words, key=get_count)[0]
    # return max(max(words, key=lambda x:len(set(x))), key=get_lex_order)
