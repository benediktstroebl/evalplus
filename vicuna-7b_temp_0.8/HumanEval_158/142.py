
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_len = len(max(words, key=len))
    max_word = [x for x in words if len(x) == max_len]
    if max_word:
        return max_word[0]
    else:
        return "0"

a = [("name", "of", "string"), ("name", "enam", "game"), ("aa", "bb", "cc")]
print(find_max(a))