
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    if words == []:
        return ""
    elif len(words) == 1:
        return words[0]

    words.sort(key=len)

    longest = words[-1]
    unique = len(set(longest))

    for word in words:
        if len(set(word)) > unique:
            unique = len(set(word))
            longest = word

    return longest

