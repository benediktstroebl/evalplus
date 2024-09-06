
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Your code goes here
    count = 0
    ans = ""
    for word in words:
        word = word.lower()
        if len(set(word)) > count:
            count = len(set(word))
            ans = word
        elif len(set(word)) == count:
            if word < ans:
                ans = word
    return ans

