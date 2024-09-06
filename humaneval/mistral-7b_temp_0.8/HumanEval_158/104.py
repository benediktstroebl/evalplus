
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def isUnique(word):
        hash_table = {}
        for letter in word:
            if letter in hash_table:
                return False
            else:
                hash_table[letter] = True
        return True

    max_str = ""
    for i in words:
        if isUnique(i):
            if len(i) > len(max_str):
                max_str = i
    return max_str


