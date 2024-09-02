
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if words:
        word_count = {}
        for word in words:
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1
        max_value = max(word_count.values())
        for key, value in word_count.items():
            if value == max_value:
                if len(key) > len(max_string):
                    max_string = key
                elif len(key) == len(max_string) and key < max_string:
                    max_string = key
                else:
                    return max_string
        return max_string
    else:
        return ""
