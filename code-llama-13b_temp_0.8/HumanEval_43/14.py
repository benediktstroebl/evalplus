

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
    # Make sure input is a list.
    if not isinstance(l, list):
        print("Input is not a list.")
        return

    # Check if there are more than one element in the list.
    if len(l) < 2:
        print("Input list does not have at least 2 elements.")
        return

    # Go through each element in the list
    for i in range(len(l)):
        # If the element is 0, check if the list has another element that is 0
        if l[i] == 0 and l.count(0) == 2:
            return True
        # Else, check if the element's complement is in the list.
        if l[i] != 0:
            if l[i] * -1 in l:
                return True
    return False
