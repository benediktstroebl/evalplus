
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

    # list of words
    words = ["name", "of", "string"]

    # initialize count of each unique char in each word
    count = {}

    # for each word in the list
    for word in words:

        # initilize counter to 0
        counter = 0

        # for each char in the word
        for char in word:
            # if the char is not in count
            if char not in count:
                # set the counter to 1
                count[char] = 1
            # else increment the counter
            else:
                count[char] += 1

    # create an empty set
    unique = set()

    # for each char in count
    for char in count:
        # add the char to the set
        unique.add(char)

    # create an empty list
    answer = []

    # for each word
    for word in words:
        # if the number of unique chars in the word is equal to the length of the word
        if len(unique) == len(word):
           
