
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Write a code to find maximum number of unique characters in a string
    max_chars = 0
    max_word = ""
    for word in words:
        count_chars = 0
        for char in word:
            if char.isalpha():
                count_chars += 1
        max_chars = max(max_chars, count_chars)
        if max_chars > words[0].count("a"):
            max_word = word
            max_chars = count_chars
    return max_word
