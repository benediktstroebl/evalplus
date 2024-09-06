
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
    words.sort()
    print(words)
    max = 0
    for word in words:
        counter = 0
        for letter in word:
            if letter not in word[:word.index(letter) + 1]:
                counter += 1
        if counter > max:
            max = counter
            max_word = word
    return max_word

