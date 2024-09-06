

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
    # init empty set to store the sum of pairs
    sum_set = set()
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            # get the sum of the two numbers and store it into sum_set
            sum_set.add(l[i] + l[j])

    # check if there is 0 in sum_set
    return 0 in sum_set

