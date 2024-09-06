

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

    # a list of the indices of numbers we've seen before
    seen_so_far = []

    for i in range(len(l)):

        # current number
        number = l[i]

        # check if it's in seen_so_far
        if i in seen_so_far:

            # if so, ignore it
            continue

        # otherwise, check if its complement is in the list
        complement = 0 - number

        if complement in l:

            # if so, return true
            return True

        # otherwise, add its index to seen_so_far
        seen_so_far.append(i)

    # if we've made it to the end of the list without returning True,
    # return False
    return False

