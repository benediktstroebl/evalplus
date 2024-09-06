
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    result = ""
    maxUnique = 0
    maxUniqueIndex = 0

    for index, word in enumerate(words):
        uniqueCount = 0
        for w in word:
            if w not in result:
                uniqueCount += 1
        if uniqueCount > maxUnique:
            maxUnique = uniqueCount
            maxUniqueIndex = index
            result = word
    return words[maxUniqueIndex]
