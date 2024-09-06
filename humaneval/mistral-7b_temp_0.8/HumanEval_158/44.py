
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # TODO: Your code goes here
    max_count = 0
    max_word = ""
    for word in words:
        count = 0
        for letter in word:
            if letter not in word[0:count]:
                count += 1
        if count > max_count:
            max_word = word
            max_count = count
    return max_word
