
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ''
    max_char_count = 0
    result = ''
    for word in words:
        count = 0
        for letter in word:
            if word.count(letter) > count:
                count = word.count(letter)
                result = word
        if count > max_char_count:
            max_char_count = count
            result = word
    return
