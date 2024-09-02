
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
    max_chars = {}
    for word in words:
        chars = set(word)
        if chars in max_chars:
            max_chars[chars].append(len(word))
        else:
            max_chars[chars] = [len(word)]
        if len(chars) > len(max_words[0][0]):
            max_words[0] = [max_words[0][1], word]
        else:
            max_words.append([word, max_words[0][0]])
    return max_words[0][1]
