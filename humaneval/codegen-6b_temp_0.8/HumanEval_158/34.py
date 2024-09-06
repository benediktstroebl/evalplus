
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_chars = 0
    max_char = ""
    for word in words:
        if len(word) > max_chars:
            max_chars = len(word)
            max_char = word

    # for word in words:
    #     if len(set(word.lower())) > max_chars:
    #         max_chars = len(set(word.lower()))
    #         max_char = word

    # for word in words:
    #     seen = {}
    #     for char in word:
    #         if char in seen:
    #             seen[char] += 1
    #         else:
    #             seen[char] = 1
    #     if len(seen) > max_chars:
    #         max_chars = len(seen)
    #         max_char = word
    #     if len(seen) == max_chars:
    #         if word < max_char:
    #             max_chars = len(seen)
    #             max_char = word

    print(max_char)

