
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_index = 0
    max_word = ""
    for i in range(len(words)):
        count = 0
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                count += 1
        if count > max_index:
            max_index = count
            max_word = words[i]
    return max_word
