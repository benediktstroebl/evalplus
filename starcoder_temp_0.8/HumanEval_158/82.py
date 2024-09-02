
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # YOUR CODE HERE
    word_dict = {}
    max_word = words[0]
    for word in words:
        word_dict[word] = len(set(word))
        if word_dict[max_word] < word_dict[word]:
            max_word = word
    return max_word

