
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # sort the strings and get the first one
    lis = sorted(words)
    max_unique_char_word = lis[0]

    for word in lis[1:]:
        # get the number of unique characters in the current word
        unique_char_count = get_unique_char_count(word)

        # get the number of unique characters in the max_unique_char_word
        unique_char_count_max = get_unique_char_count(max_unique_char_word)

        if unique_char_count > unique_char_count_max:
            max_unique_char_word = word
        elif unique_char_count == unique_char_count_max:
            if word < max_unique_char_word:
                max_unique_char_word = word

    return max_unique_char_word

