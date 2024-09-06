
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # create a set of all characters in the words
    char_set = set(word.lower() for word in words)
    # use a defaultdict to count the number of occurrences of each character
    count = defaultdict(int)
    # iterate over the words
    for word in words:
        # iterate over the characters in the word
        for char in word:
            count[char] += 1
    # find the word with the highest number of unique characters
    max_count = max(count.values())
    max_word = "".join(char for char in word if count[char] == max_count)
    return max_word