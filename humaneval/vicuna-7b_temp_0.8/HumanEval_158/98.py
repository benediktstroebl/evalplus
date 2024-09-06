
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    words = set(words)
    max_len = max(len(word) for word in words)
    max_word = max(word for word in words if len(word) == max_len)
    return max_word

a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]
c = [3, 4, 5, 6, 7]

print(sorted(a, key=lambda x: find_max(filter(lambda x: x == x, [a, b, c]))))
