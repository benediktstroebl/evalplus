
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # 1st solution
    # Maximum of unique characters = Length of string
    # Word with max chars must be the shortest in length

    # store the length of longest string
    max_len = 0
    # store the longest string
    longest_string = ''
    # iterate through each word
    for word in words:
        # check if word has more characters than current max
        if len(word) > max_len:
            # store word
            longest_string = word
            # update max length
            max_len = len(word)

    return longest_string

