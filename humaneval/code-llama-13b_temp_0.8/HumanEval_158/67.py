
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def uniq_chars(string):
        return len(set(string))

    unique_char_counts = [uniq_chars(w) for w in words]
    max_count_index = unique_char_counts.index(max(unique_char_counts))
    return words[max_count_index]
