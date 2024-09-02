

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

    # set up a dictionary to store the elements as keys
    # and the number of times they occur as values
    num_count = {}
    for num in l:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # if there is only one element
    if len(num_count) < 2:
        return False

    # if there are two elements
    if len(num_count) == 2:
        # see if they sum to zero
        for num in num_count:
            if num + num == 0:
                return True
        return False

    # if there is more than two elements
    if len(num_count) > 2:
        # set up a list of the keys
        # sort the list
        num_list = list(num_count.keys())
        num_list.sort()

        # set up a set to store the sums that have been found so far
        sums = set()

        # check each pair to see if their sum is in the set
        for i in range(len(num_list) - 1):
            for j in range(i + 1, len(num_list)):
                pair_sum = num_list[i] + num_list[j]
                if pair_sum in sums:
                    return True
                sums.add(pair_sum)

        # if no sum is found return False
        return False
