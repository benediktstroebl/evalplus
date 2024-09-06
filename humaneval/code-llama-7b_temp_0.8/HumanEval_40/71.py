

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
    # first we need to find the sums of all pairs
    pair_sums = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            pair_sums.append(l[i] + l[j])

    # now we find all the triples where all three are distinct, and
    # where the sum of all three is zero.
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                if l[i] + l[j] + l[k] == 0 and l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                    return True
    return False

