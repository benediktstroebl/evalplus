
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    a = {}
    for i in words:
        for j in i:
            if j not in a:
                a[j] = 1
            else:
                a[j] += 1

    print(a)
    sorted_a = sorted(a, key=a.get, reverse=True)
    print(sorted_a)
    max_word = words[sorted_a.index(0)]
    return max_word
