
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # loop through the words and count the number of unique chars
    # in each word
    word_counts = [(word, sum([len(set(w)) for w in words])) for word in words]

    # get the words with the maximum number of unique characters
    max_word_counts = [x for x in word_counts if x[1] == max(word_counts, key=lambda x: x[1])[1]]

    # if there is more than one, return the first one in lexicographical order
    return max(max_word_counts, key=lambda x: x[0])[0]
