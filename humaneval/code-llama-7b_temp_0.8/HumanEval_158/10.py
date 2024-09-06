
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    longest = len(set(words[0]))
    final_word = ""
    for word in words:
        if len(set(word)) > longest:
            longest = len(set(word))
            final_word = word
        elif len(set(word)) == longest:
            if word < final_word:
                final_word = word
    return final_word
