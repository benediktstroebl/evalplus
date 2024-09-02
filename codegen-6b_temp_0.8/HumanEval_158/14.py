
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = []
    word_lengths = [len(w) for w in words]
    for index, word in enumerate(words):
        char_count = {}
        for character in word:
            char_count[character] = char_count.get(character, 0) + 1
        max_chars.append((word, word_lengths[index], char_count))
    max_chars = sorted(max_chars, key=lambda tup: tup[1])
    max_count = max([tup[2] for tup in max_chars])
    max_words = [tup[0] for tup in max_chars if tup[2] == max_count]
    max_words = sorted(max_words, key=lambda tup: tup[1])
    return max_words[0]
