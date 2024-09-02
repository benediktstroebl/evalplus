
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def find_unique_char(word):
        unique_char = 0
        char_set = set()

        for char in word:
            if char not in char_set:
                char_set.add(char)
                unique_char += 1

        return unique_char

    unique_word = words[0]
    max_unique_char = find_unique_char(unique_word)

    for word in words:
        unique_char = find_unique_char(word)

        if unique_char > max_unique_char:
            max_unique_char = unique_char
            unique_word = word

    return unique_word
