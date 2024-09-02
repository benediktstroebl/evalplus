
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # YOUR CODE GOES BELOW HERE #
    # Don't modify the line above

    # Write your code here
    max_length = 0
    max_word = ""
    for word in words:
        count = 0
        for i in word:
            if word.count(i) == 1:
                count += 1
        if count > max_length:
            max_length = count
            max_word = word

    # Write your code here
    # Don't modify the line above

    return max_word

