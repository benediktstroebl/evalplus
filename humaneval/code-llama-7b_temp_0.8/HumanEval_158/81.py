
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
    elif len(words) == 2:
        word1, word2 = words[0], words[1]
        if len(set(word1)) > len(set(word2)):
            return word1
        elif len(set(word1)) < len(set(word2)):
            return word2
        else:
            if word1 < word2:
                return word2
            else:
                return word1
    else:
        word = words[0]
        for i in range(1, len(words)):
            if len(set(words[i])) > len(set(word)):
                word = words[i]
            elif len(set(words[i])) == len(set(word)):
                if words[i] < word:
                    word = words[i]
        return word
