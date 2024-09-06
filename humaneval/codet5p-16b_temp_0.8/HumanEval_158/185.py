
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    
    counts = {}
    for word in words:
        counts[word] = 0
        for letter in word:
            if letter in counts:
                counts[letter] += 1

    if len(counts) == 0:
        return None

    maximum = max(counts.values())
    max_words = [word for word in words if counts[word] == maximum]
    
    return min(max_words)
