
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
    else:
        max = words[0]
        for word in words:
            if word == max:
                continue
            elif len(set(word)) > len(set(max)):
                max = word
            elif len(set(word)) == len(set(max)):
                if word < max:
                    max = word
        return max

