
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Your code here

    sorted_words = sorted(words)
    max_count = len(sorted_words[0])
    for word in sorted_words:
        if len(word) > max_count:
            max_count = len(word)

    max_unique_chars = ""

    for word in sorted_words:
        if len(word) == max_count:
            if len(set(word)) > len(set(max_unique_chars)):
                max_unique_chars = word

    return max_unique_chars
