
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Use a defaultdict to count the number of unique characters for each word
    char_counts = defaultdict(int)
    max_word = ""
    max_count = 0
    for word in words:
        for c in word:
            char_counts[c] += 1
        max_count = max(max_count, char_counts[c] for c in word)
        if max_count > words[0].count(c) for c in word:
            return max_word
    return max_word