

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

    # sort the list.
    l.sort()
    # make 3 pointers, left, mid and right.
    left, mid, right = 0, 1, 2
    # loop until the mid pointer has not reached the end.
    while mid < len(l):
        # if the current element is 0, return True.
        if l[mid] == 0:
            return True
        # else, set the left and right pointers to 1 and length - 1.
        left, right = 1, len(l) - 1
        # loop while the left pointer is less than the right pointer.
        while left < right:
            # if the left pointer element and the right pointer element sum to 0,
            # return True.
            if l[left] + l[right] == -l[mid]:
                return True
            # else if the left pointer element is less than the right element,
            # increment the left pointer.
            if l[left] < -l[mid]:
                left += 1
            # else, decrement the right pointer.
            else:
                right -= 1
        # increment the mid pointer.
        mid += 1

    # return False.
    return False
