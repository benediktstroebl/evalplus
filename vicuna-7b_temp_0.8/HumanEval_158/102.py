
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""
    word = words[0]
    count = {}
    for word in words:
        for char in word:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    max_chars = max(count, key=count.get)
    return "".join([word[i:i+1] for i, char in enumerate(word) if char in count and count[char] == max_chars])
