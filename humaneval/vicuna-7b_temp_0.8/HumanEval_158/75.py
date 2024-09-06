
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # sort the words by number of unique characters
    words = sorted(words, key=lambda x: len(set(x)), reverse=True)

    # check if there is only one word
    if len(words) == 1:
        return words[0]

    # check if there are two words with maximum number of unique characters
    if len(words) == 2:
        # if they are in lexicographical order, return the first word
        if words[0] < words[1]:
            return words[0]
        else:
            return words[1]

    # check if there are more than two words with maximum number of unique characters
    for i in range(2, len(words)):
        # check if there is a swap that makes them in lexicographical order
        if words[i] > words[0] and words[i] < words[1]:
            # swap the words
            words[0], words[1] = words[1], words[0]
            # check if the new order is lexicographical
            if words[0] < words[i]:
                return words[0]
            else:
                return words[1]

    # return the first word if there is no lexicographical order
    return words[0]
