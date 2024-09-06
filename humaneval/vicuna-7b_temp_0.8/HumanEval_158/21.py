
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    word_count = {}
    for w in words:
        char_set = set(w)
        for c in char_set:
            if c not in word_count:
                word_count[c] = 1
            else:
                word_count[c] += 1
    max_set = max(word_count.iteritems(), key=lambda x: x[1])
    return ''.join([c for c in max_set[0] if c in 'abcdefghijklmnopqrstuvwxyz'])
