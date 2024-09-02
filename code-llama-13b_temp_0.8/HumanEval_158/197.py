
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    result_word = ""
    max_value = 0
    for word in words:
        result = dict()
        for char in word:
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
        result_value = sum(result.values())
        if result_value >= max_value:
            if result_value != max_value:
                result_word = word
                max_value = result_value
            else:
                result_word = min([word, result_word])
    return result_word
