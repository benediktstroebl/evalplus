
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # We can do it in O(n log n)

    # A dictionary to count each character in each string
    # O(n)
    dictionary = {}
    for word in words:
        for letter in word:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    # print(dictionary)
    # Create a list of tuples (count, word)
    # O(n)
    list_tuples = []
    for word in words:
        unique_chars = 0
        for letter in word:
            if dictionary[letter] == 1:
                unique_chars += 1
        list_tuples.append((unique_chars, word))
    # print(list_tuples)
    # Sort list based on count, then word
    # O(n log n)
    sorted_list = sorted(list_tuples)
    # print(sorted_list)
    # return the last item
    return sorted_list[-1][1]

