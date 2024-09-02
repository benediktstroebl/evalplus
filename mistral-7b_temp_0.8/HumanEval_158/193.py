
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    print(type(words))
    for word in words:
        print(word)

    for word in words:
        print(word)
        count = {}
        count2 = {}
        for letter in word:
            count2[letter] = 0
            count[letter] = count.get(letter,0) + 1
            print(letter, ": ", count[letter])

        for key in count.keys():
            print(key, ": ", count[key])
        for key in count2.keys():
            print(key, ": ", count2[key])

    count2 = {key: count[key] for key in count if count[key] == count[max(count)]}
    print(count2)
    if len(count2) > 1:
        count2 = sorted(count2)
        print(count2)
    print(min(count2))

    return words


