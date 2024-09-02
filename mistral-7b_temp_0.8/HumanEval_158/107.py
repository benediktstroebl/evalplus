
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
        seen = set()
        for char in word:
            if char in seen:
                return 0
            seen.add(char)
        return 1

    words.sort()
    max_word = words[0]
    max_count = count_unique_chars(words[0])
    for i in range(1, len(words)):
        word = words[i]
        if count_unique_chars(word) > max_count:
            max_word = word
            max_count = count_unique_chars(word)
        elif count_unique_chars(word) == max_count:
            max_word = min(max_word, word)
    return max_word

