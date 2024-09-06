
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    ans = ""
    for word in words:
        counter = {}
        for i in word:
            if i not in counter.keys():
                counter[i] = 1
            else:
                counter[i] += 1
        if len(counter) > len(ans) or (len(counter) == len(ans) and word < ans):
            ans = word
    return ans

