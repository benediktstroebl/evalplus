
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    wordList = words
    longestWord = []

    for word in wordList:
        wordSet = set()
        wordList.sort()
        for letter in word:
            if letter not in wordSet:
                wordSet.add(letter)

        longestWord.append(word)

    longestWord.sort()

    return longestWord[-1]
