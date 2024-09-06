
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # create an empty list
    max_ = []
    # loop through the list of strings
    for word in words:
        # if the word's length is equal to the length of the list max_
        if len(word) == len(max_):
            # and the word is less than the value at the end of the max_ list
            if word < max_[-1]:
                # then remove the last value from the list
                max_.pop()
                # and append the word to the end of the list
                max_.append(word)
        # if the word's length is greater than the length of the list max_
        elif len(word) > len(max_):
            # then clear the list max_
            max_.clear()
            # and append the word to the list
            max_.append(word)
    # return the first value in the list
    return max_[0]

