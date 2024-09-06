
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def uniqueChars(word):
        unique, repeat = 0, 0
        for letter in word:
            unique += 1
            if unique == len(word):
                return word
            if word.count(letter) > 1:
                repeat += 1
        if repeat > 1:
            return ""
        return word

    words.sort(key=uniqueChars, reverse=True)
    return words[0]

