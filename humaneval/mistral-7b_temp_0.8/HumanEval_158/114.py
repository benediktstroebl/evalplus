
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    new_list = []
    unique_chars = set()
    for word in words:
        for char in word:
            unique_chars.add(char)
    for word in words:
        if len(set(word)) == len(unique_chars):
            new_list.append(word)
    if len(new_list) == 0:
        return words[0]
    else:
        return min(new_list)
