
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # This is a very simple problem that has been solved in a group of students
    # and we were not using set instead of a dictionary. We used a for loop to
    # compute the unique count for each word and then got the max count word from
    # the list.
    max_word = ""
    count = {}
    for word in words:
        unique = {}
        for char in word:
            unique[char] = unique.get(char, 0) + 1
        count[word] = unique
    for word in words:
        if len(count[word]) > len(count[max_word]):
            max_word = word
    return max_word


"""
    Find three number whose sum is equal to zero
    Given a list of numbers, find the first four numbers whose sum is equal to zero.
    For example, if the given numbers are {1, 2, -3, -4,4, 0, -3, 0, -4, -1},
    then your program should return {8, 3, -4, -2}, as -4 + 1 + 2 + 4 = 0
    This is just an interesting problem you can get it.
    If you think that the input list contains only integers, then try to find
     a solution without using Type casting.

"""
