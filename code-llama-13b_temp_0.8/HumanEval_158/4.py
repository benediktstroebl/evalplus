
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if type(words) != list:
        raise TypeError("Only a list of words is accepted")
    words = sorted(words, key=lambda x: len(set(x)), reverse=True)
    chars = {char for char in words[0]}
    for word in words[1:]:
        new_chars = {char for char in word}
        if len(new_chars) < len(chars):
            break
        elif len(new_chars) == len(chars):
            chars = new_chars
        else:
            chars = new_chars
    return words[0]

