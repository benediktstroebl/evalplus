

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
    # Store the found solutions in a set. This is to avoid having duplicates
    # due to numerical precision issues.
    found = set()

    # If there are no elements, return false.
    if len(l) == 0:
        return False

    # Otherwise, check the sums for each element.
    for i, element in enumerate(l):

        # Iterate over the elements after the current one.
        for other_element in l[i + 1:]:
            if -element == other_element:
                found.add((element, other_element))

    return len(found) > 0

