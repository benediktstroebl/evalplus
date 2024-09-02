
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Sort words in alphabetical order, e.g. ['aa', 'aa', 'aaa'] -> ['aa', 'aaa']
    words.sort()
    # Start from the first word, if current word contains all unique characters,
    # then we found the longest word with unique characters.
    unique_chars = 0
    max_chars = 0
    max_word = ''
    for word in words:
        current_chars = 0
        for letter in word:
            if letter not in word:
                current_chars += 1
        if current_chars > unique_chars:
            unique_chars = current_chars
            max_chars = len(word)
            max_word = word
    return max_word
