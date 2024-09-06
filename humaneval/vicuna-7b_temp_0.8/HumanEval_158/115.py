
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word = ""
    max_uniq_chars = 0
    max_index = 0
    for i in range(len(words)):
        count = 0
        for j in range(i+1, len(words)):
            if words[j] == words[i]:
                count += 1
        if count > max_uniq_chars:
            max_word = words[i]
            max_uniq_chars = count
            max_index = i
    return max_word