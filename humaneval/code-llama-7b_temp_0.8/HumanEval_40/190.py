

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # initialize list of sums and sum variable
    sum_list = [0]
    sum = 0

    # loop over input list and add elements to sum variable
    for num in l:
        sum += num
        # add new sum to list of sums if unique
        if sum not in sum_list:
            sum_list.append(sum)

    # return True if 0 sum is in list of sums
    return 0 in sum_list

