
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if len(words) == 0:
        return None
    max_word = words[0]
    max_length = len(max_word)
    for word in words:
        length = len(word)
        if length > max_length:
            max_word = word
            max_length = length
        elif length == max_length:
            if word < max_word:
                max_word = word
            elif word == max_word:
                pass
        else:
            pass
    return max_word

