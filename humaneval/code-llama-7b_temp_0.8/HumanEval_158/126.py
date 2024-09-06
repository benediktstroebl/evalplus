
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # your code here
    unique = {}
    for word in words:
        for char in word:
            if char not in unique:
                unique[char] = 1
            else:
                unique[char] += 1
    max_count = max(unique.values())
    result = ''
    for char in words:
        for key, value in unique.items():
            if value == max_count:
                if len(key) > len(result):
                    result = key
                elif len(result) == 0:
                    result = key
    return result


