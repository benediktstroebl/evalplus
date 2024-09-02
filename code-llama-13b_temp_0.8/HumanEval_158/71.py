
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

    if len(words) == 1:
        return words[0]

    words = sorted(words)
    # print(words)
    # words = ["name", "enam", "game"]
    max_count = 0
    for i in range(len(words) - 1):
        current_count = len(set(words[i]))
        next_count = len(set(words[i+1]))
        if current_count > max_count:
            max_count = current_count
            candidate = words[i]

        if current_count > next_count:
            max_count = next_count
            candidate = words[i+1]

    return candidate

