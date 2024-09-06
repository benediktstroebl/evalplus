
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    length = len(words)
    if length == 0:
        return 0
    elif length == 1:
        return words[0]
    else:
        first = words[0]
        second = words[1]
        first_char_dict = {}
        second_char_dict = {}
        for i in range(len(first)):
            if first[i] not in first_char_dict:
                first_char_dict[first[i]] = 1
            else:
                first_char_dict[first[i]] += 1
        for j in range(len(second)):
            if second[j] not in second_char_dict:
                second_char_dict[second[j]] = 1
            else:
                second_char_dict[second[j]] += 1
        if len(first_char_dict) > len(second_char_dict):
            return first
        elif len(first_char_dict) < len(second_char_dict):
            return second
        else:
            if first < second:
                return first
            else:
                return second

