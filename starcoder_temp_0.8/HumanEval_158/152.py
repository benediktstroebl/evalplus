
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # 1. Create a dictionary to store the number of unique characters
    #    for each word in the list.
    # 2. Loop through the list of words
    # 3. For each word, find the number of unique characters
    # 4. Compare the number of unique characters with the previous number
    # 5. Return the word with maximum number of unique characters
