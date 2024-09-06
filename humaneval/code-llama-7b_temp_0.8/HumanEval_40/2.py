

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
    # use a set to keep track of elements that have been seen, and
    # also use a set to keep track of what's left to check
    seen = set()
    unseen = set(l)

    for elem in l:
        # check if (0 - elem) is in the unseen set
        if (0 - elem) in unseen:
            # return True if so
            return True
        # otherwise add elem to seen
        seen.add(elem)
        # and remove it from unseen
        unseen.remove(elem)

    # if we've reached this point, we've checked every element in l
    # and there are no triples that sum to zero
    # return False in this case
    return False

