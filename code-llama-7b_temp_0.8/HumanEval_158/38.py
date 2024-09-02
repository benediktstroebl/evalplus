
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # TODO: Write your function here
    if words == []:
        return ''

    word_max = words[0]
    unique_characters = []
    for word in words:
        if len(unique_characters) < len(set(word)):
            unique_characters = list(set(word))
            word_max = word
        elif len(unique_characters) == len(set(word)):
            if word < word_max:
                unique_characters = list(set(word))
                word_max = word
    return word_max

