
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Your code here
    unique_dict = {}
    for word in words:
        unique = []
        for char in word:
            if char not in unique:
                unique.append(char)
        unique_dict[word] = len(unique)

    unique_dict = sorted(unique_dict.items(), key=lambda x: x[1])
    max_value = unique_dict[-1][1]
    words = [word for word, count in unique_dict if count == max_value]

    return words[0]

