
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    all_unique_letters = {}
    for word in words:
        # Slots is a dictionary to keep the number of times each letter appears
        # For each word
        # 1) init a slot for each letter in the word
        # 2) if it already exists then increase its value by one
        for letter in word:
            if letter in all_unique_letters:
                all_unique_letters[letter] += 1
            else:
                all_unique_letters[letter] = 1
    max_unique = 0
    max_unique_word = ""
    # Traverse the dict to find the max_unique and the corresponding word
    for key in all_unique_letters:
        if all_unique_letters[key] > max_unique:
            max_unique = all_unique_letters[key]
            max_unique_word = key
    return max_unique_word
