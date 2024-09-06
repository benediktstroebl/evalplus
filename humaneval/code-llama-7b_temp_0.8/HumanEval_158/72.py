
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

    counter = len(set(words[0]))
    result = words[0]
    for word in words[1:]:
        current_counter = len(set(word))
        if current_counter > counter or (current_counter == counter and word < result):
            counter = current_counter
            result = word

    return result
