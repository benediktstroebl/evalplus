
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    new_list = []
    for word in words:
        count_unique = {}
        for char in word:
            if char not in count_unique:
                count_unique[char] = 1
            else:
                count_unique[char] += 1
        max_char = max(count_unique, key=count_unique.get)
        new_list.append(max_char)
    return "".join(new_list)
    
