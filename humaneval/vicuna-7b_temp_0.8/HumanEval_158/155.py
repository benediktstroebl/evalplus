
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # count the number of unique characters in each string
    unique_chars_count = {}
    for word in words:
        for char in word:
            if char in unique_chars_count:
                unique_chars_count[char] += 1
            else:
                unique_chars_count[char] = 1

    # initialize a list to store the words with maximum unique characters
    max_list = []

    # loop through the list of strings
    for word in words:
        # find the number of unique characters in the word
        unique_chars_count[word] = len(set(word))

        # if the word has more unique characters than the current max
        if max_list and max_list[-1][::-1] > word:
            max_list = [word]
        else:
            max_list.append(word)

    # return the first word in the max list
    return max_list[0]
