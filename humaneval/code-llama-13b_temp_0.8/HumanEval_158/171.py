
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    if type(words) is not list or len(words) < 1:
        return None

    result = 0
    result_word = ""

    for word in words:
        if type(word) is not str:
            return None

        unique_letters = []

        for letter in word:
            if letter not in unique_letters:
                unique_letters.append(letter)

        if len(unique_letters) > result:
            result = len(unique_letters)
            result_word = word

    return result_word

