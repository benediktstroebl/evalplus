
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Create a dictionary with each word as key and character count as value
    dictionary = {}
    for word in words:
        for char in word:
            if char not in dictionary:
                dictionary[char] = 0
            dictionary[char] += 1

    # Get the words with maximum unique characters
    max_words = [word for word, count in dictionary.items() if count == max(dictionary.values())]

    # Return the first word in lexicographical order
    return min(max_words)

