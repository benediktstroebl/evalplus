

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
    # Set up a set to keep track of values seen
    seen = set()
    # Iterate through list
    for num in l:
        # If the number is already in the set, we know that we've
        # seen it before and therefore can return True
        if num in seen:
            return True
        # Otherwise, add the number to the set
        seen.add(num)
    # If we have gone through the whole list without returning True,
    # return False
    return False

