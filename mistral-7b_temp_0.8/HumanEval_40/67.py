

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
    # if l is empty return false
    if len(l) < 3:
        return False
    # create empty set for triples
    triples = set()
    for n1 in l:
        for n2 in l:
            for n3 in l:
                # check if n1 + n2 + n3 is zero
                if n1 + n2 + n3 == 0:
                    # if triples exist return true
                    if (n1, n2, n3) in triples:
                        return True
                    else:
                        # if triples do not exist add triples to set
                        triples.add((n1, n2, n3))
    return False

