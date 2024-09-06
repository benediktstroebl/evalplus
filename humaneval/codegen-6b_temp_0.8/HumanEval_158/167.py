
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # We are sorting the list in order to get the maximum. 
    # If the list is already sorted, lexicographical order is guaranteed to 
    # give us the correct answer.
    sorted_words = sorted(words)
    max_len = len(sorted_words[0])
    for word in sorted_words[1:]:
        if len(word) > max_len:
            max_len = len(word)
    
    results = []
    for word in sorted_words:
        if len(word) == max_len:
            results.append(word)
            
    return sorted(results)[0]

assert find_max(["name", "of", "string"]) == "string"
assert find_max(["name", "enam", "game"]) == "enam"
assert find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"

