
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    max_word = words[0]
    max_chars = set()
    max_chars.update(words[0])
    for word in words[1:]:
        cur_chars = set(word)
        if len(cur_chars) > len(max_chars):
            max_chars = cur_chars
            max_word = word
        elif len(cur_chars) == len(max_chars):
            if word < max_word:
                max_word = word

    return max_word

