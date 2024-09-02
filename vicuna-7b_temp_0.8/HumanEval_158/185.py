
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # use a defaultdict to count the number of unique characters
    # for each word
    counts = defaultdict(int)
    for word in words:
        for char in word:
            counts[char] += 1

    max_char = max(counts.values(), key=counts.get)
    max_word = ""
    for char in max_char:
        # check if the current word has the same characters as the max_char
        if max_char == char:
            max_word += char
        else:
            break
    return max_word
