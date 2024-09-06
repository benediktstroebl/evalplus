
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # sort the list in reverse order of frequency of characters
    word_freq = {}
    for word in words:
        for char in word:
            if char in word_freq:
                word_freq[char] += 1
            else:
                word_freq[char] = 1
    word_freq_rev = {k: v for k, v in word_freq.items()}
    sorted_words = sorted(word_freq_rev, reverse=True)
    max_word = ""
    for word in sorted_words:
        if max_word == "":
            max_word = word
        elif word != max_word:
            return max_word
    return max_word
