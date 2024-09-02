
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    #step 1. create a dictionary of unique characters of each word.
    dictionary = {}
    for word in words:
        temp = set(word)
        dictionary[word] = list(temp)
    #step 2.  get the value of each key (string) in the dictionary and sort them.
    values = sorted(dictionary.values(), key=len)
    #step 3. return the key of the first item in the sorted list.
    return values[0][0]
