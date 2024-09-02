

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
    # return False

    # start with an empty list
    # set the index to be 0
    # while the index is less than the length of the list:
        # set a variable equal to the value at the index
        # set the index to be equal to the index + 1
        # iterate over the list with an inner loop
            # if the value at the index is the same as the value stored in the variable:
                # return false
            # if the value at the index is equal to 0 minus the value stored in the variable:
                # return True
    # return False

    # for each item in list
    # check if item + any other item in list is equal to 0
    # if yes, return True
    # otherwise return False


    # # we don't care what the second value is, just need to check if it is there
    # for x in l:
    #     if 0 - x in l:
    #         return True
    # return False


    # for each item in list
    # check if item + any other item in list is equal to 0
    # if yes, return True
    # otherwise return False
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False

