

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
    # create a dictionary of values and their counts.
    # store the dictionary in a variable named 'dic'.

    # iterate through the dictionary
    # for each element, check if it's complement exists in the dictionary.

    # if it does, return True.
    # else, return False

    dic = {}
    for i in l:
        dic[i] = 1
    for i in l:
        if i * -1 in dic.keys():
            return True
    return False

