
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    max_dict = {}
    max_length = 0
    max_word = ""

    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            max_word = word
        elif len(word) == max_length:
            max_word = min(word, max_word)

    for word in words:
        count = 0
        unique = set()
        for letter in word:
            if letter not in unique:
                count += 1
                unique.add(letter)
        max_dict[word] = count

    return max(max_dict.items(), key=lambda x: (x[1], x[0]))[0]


