

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

    # assume we have a list of 4 unique numbers
    # [1, 3, -2, 1]

    # iterate through the list
    # O(n)
    for i in range(len(l)):
        # iterate through the list again
        # O(n)
        for j in range(len(l)):
            # iterate through the list once more
            # O(n)
            for k in range(len(l)):
                # check if i, j, and k sum to zero
                # O(1)
                if l[i] + l[j] + l[k] == 0:
                    # check if i, j, and k are all distinct
                    # O(1)
                    if i != j and i != k and j != k:
                        return True
    return False
