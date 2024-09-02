

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
    # Start with an empty dictionary to maintain count of distinct triplets
    count = {}
    # loop through list
    for i in l:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    # Now check for triplets in the dictionary
    for i in count:
        if -i in count and (count[-i] > 1 or count[i] > 2):
            return True
    return False

