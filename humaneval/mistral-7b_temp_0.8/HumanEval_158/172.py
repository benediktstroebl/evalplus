
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def count_unique_chars(word):
        return len(set(word))

    unique_words = [count_unique_chars(word) for word in words]

    max_words = [words[i] for i in range(len(words)) if unique_words[i] == max(unique_words)]
    max_word = max(max_words)

    return max_word

