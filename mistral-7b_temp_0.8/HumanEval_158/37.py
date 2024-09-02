
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

    #solution
    arr = []
    words.sort(key=len)
    for word in words:
        arr.append(set(word))
    result = arr[0]
    for char in arr:
        if len(char) > len(result):
            result = char
        elif len(char) == len(result):
            result = min(result, char, key=str.lower)
    return result

    #solution2
    return max(words, key=len)

