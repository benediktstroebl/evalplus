
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words)==0:
        return ""
    max_char=words[0]
    for word in words[1:]:
        if max_char>word:
            continue
        if len(set(max_char))>len(set(word)):
            max_char=word
    return max_char
