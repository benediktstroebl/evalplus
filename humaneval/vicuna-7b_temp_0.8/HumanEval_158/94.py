
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    seen = set()
    max_word = ""
    for word in words:
        chunks = word.split()
        n = len(chunks)
        for i in range(n-1, 0, -1):
            if chunks[i] in seen:
                # if a letter is repeated, the word is not unique
                break
        else:
            if n == 1:
                # if only one chunk, word is unique
                seen.add(chunks[0])
                max_word = word
            else:
                # if more than one chunk, word is not unique
                break
    return max_word