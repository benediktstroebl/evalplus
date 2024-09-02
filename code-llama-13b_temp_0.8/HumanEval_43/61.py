

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
    # make a set out of the list.
    # the set will only contain unique values.
    # do a nested loop over the set,
    # and check if the current element sums to zero with another element.

    # set = []
    #
    # for i in l:
    #     if i not in set:
    #         set.append(i)

    # for i in set:
    #     for j in set:
    #         if i != j and i+j == 0:
    #             return True
    # return False

    # variable initialization
    set_of_items = set()
    distinct_item = set()
    # first find the set of items
    for i in l:
        if i not in set_of_items:
            set_of_items.add(i)
    # then find the distinct elements
    for i in set_of_items:
        if i not in distinct_item:
            distinct_item.add(i)
    # then check for two distinct elements which add to zero
    for i in distinct_item:
        if -1*i in distinct_item:
            return True
    return False


