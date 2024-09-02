
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
    for word in words:
        unique_chars = "".join(set(word)).split()
        if len(unique_chars) > len(word_count):
            word_count = unique_chars
        if word_count not in word_count.values():
            word_count_values = sorted(word_count.values(), key=lambda x: x[::-1])
            if word_count_values[0] == word_count:
                return word
        else:
            return word
