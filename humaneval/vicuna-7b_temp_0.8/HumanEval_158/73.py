
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = max(len(word) for word in words)
    max_word = "".join(words)
    max_word = max_word.split()
    word_dict = dict(zip(max_word, range(len(max_word))))
    for word in words:
        char_count = len(word)
        for char in word:
            if char_count[word.index(char)] < char_count:
                char_count[word.index(char)] += 1
    return max_word

print(find_max(["aaa", "bbb", "ccc"]))