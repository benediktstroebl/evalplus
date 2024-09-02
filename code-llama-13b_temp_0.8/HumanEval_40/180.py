

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
    if len(l) < 3:
        return False
    # store the numbers we've seen so far in a set
    # so that we can check if a number is in the set in constant time
    seen = set()
    for num in l:
        if num not in seen:
            # if the number is not in the set, add it
            seen.add(num)
        else:
            # if the number is in the set, check if -num is also in the set
            if -num in seen:
                return True
    return False
