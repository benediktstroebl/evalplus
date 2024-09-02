
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # if not words:
    #     return ""

    # result = ""
    # unique = 0
    # for word in words:
    #     unique = len(set(word))
    #     if unique > len(set(result)):
    #         result = word
    #     elif unique == len(set(result)):
    #         if word < result:
    #             result = word
    # return result

    def max_unique(words):
        """Return word with max unique chars."""
        if not words:
            return ""

        # If it's not the first word, check if it has more unique chars than
        # the current maximum
        if words[0] != max_unique(words[1:]):
            return words[0]

        # If it is the first word, check against words[1:]
        else:
            for word in words[1:]:
                unique = len(set(word))
                if unique > len(set(words[0])):
                    return word
            return words[0]

    return max_unique(words)

