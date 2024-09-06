
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_char = []
    for word in words:
        single_word_char = {}
        for letter in word:
            if letter in single_word_char:
                single_word_char[letter] += 1
            else:
                single_word_char[letter] = 1
        max_char.append(single_word_char)
    max_index = 0
    for i in range(1, len(max_char)):
        if len(max_char[i]) > len(max_char[max_index]):
            max_index = i
        elif len(max_char[i]) == len(max_char[max_index]):
            if word[i] > word[max_index]:
                max_index = i
    return words[max_index]

