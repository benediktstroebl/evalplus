
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    length = len(words[0])
    for word in words:
        if len(word) > length:
            length = len(word)
    count = {}
    for char in words[0]:
        count[char] = 0
    for word in words:
        for char in word:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    max_count = max(count.values())
    max_keys = [key for key in count if count[key] == max_count]
    for word in words:
        for key in max_keys:
            if key not in word:
                max_keys.remove(key)
    for word in words:
        for key in max_keys:
            if key in word:
                return word
    return ""
