
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_characters = {}
    max_value = 0
    result = None
    for word in words:
        current_count = 0
        for char in word:
            if char not in unique_characters:
                unique_characters[char] = 1
                current_count += 1
            else:
                unique_characters[char] += 1
                current_count += 1

        if current_count > max_value:
            max_value = current_count
            result = word

    return result



