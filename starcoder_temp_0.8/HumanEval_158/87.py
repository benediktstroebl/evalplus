
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    counter = 0
    max_counter = 0
    word = words[0]
    for i in range(len(words)):
        if len(words[i]) > len(word):
            word = words[i]

    for i in range(len(word)):
        for j in range(len(words)):
            if i < len(words[j]) and words[j][i] not in word[i:]:
                counter += 1
        if counter > max_counter:
            max_counter = counter
            word = word[:i+1]
        counter = 0
    return word
