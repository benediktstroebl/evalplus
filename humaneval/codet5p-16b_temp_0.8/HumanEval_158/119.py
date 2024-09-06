
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_words = []
    max_unique = []

    for i in range(len(words)):
        temp = []
        count = 0
        for j in range(len(words)):
            if i!= j:
                if words[i] == words[j]:
                    count += 1
        max_unique.append(count)
        if len(max_unique) > 1 and max_unique[i] == max_unique[0]:
            max_unique.pop(0)
            max_unique.append(0)
    if max_unique.count(max(max_unique)) > 1:
        return min(words)
    else:
        for i in range(len(words)):
            if max_unique[i] == max(max_unique):
                max_words.append(words[i])
    return sorted(max_words)[0]

