
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
        longest = max(words, key=len)
        for word in words:
            if word == longest:
                continue
            else:
                unique = 0
                for char in word:
                    if char in longest:
                        unique += 1
                if unique == len(word):
                    return word
                else:
                    continue
    return longest

