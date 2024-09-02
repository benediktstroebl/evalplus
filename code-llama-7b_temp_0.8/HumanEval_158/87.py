
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # Iterate through each word in the list and find the word with maximum number of unique characters
    max_unique = words[0]
    max_unique_count = len(set(words[0]))
    for word in words[1:]:
        unique_count = len(set(word))
        if unique_count > max_unique_count:
            max_unique = word
            max_unique_count = unique_count

    # If the word with maximum number of unique characters has more than one unique character
    if len(set(max_unique)) > 1:
        return max_unique
    else:
        return ""
