

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """

    # create a dictionary called numbers that will hold all integers that appear in the list
    numbers = {}
    # loop through the list of integers
    for integer in l:
        # if the integer is in the dictionary and the sum of the integer and -1 * integer = 0
        if integer in numbers and numbers[integer] + integer == 0:
            return True
        # if the integer is not in the dictionary, add the integer to the dictionary
        if integer not in numbers:
            numbers[integer] = 0
    return False
