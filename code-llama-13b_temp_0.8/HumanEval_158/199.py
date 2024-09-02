
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_words = []
    max_char = 0
    for word in words:
        current_char = len(set(word))
        if current_char > max_char:
            max_words = [word]
            max_char = current_char
        elif current_char == max_char:
            max_words.append(word)
    return max_words[0]

