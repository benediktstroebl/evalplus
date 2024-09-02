

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
    if l == []:
        return True
    elif len(l) == 1: # if l is of length 1, return false
        return False
    else:
        c = 0
        for i in range(len(l) - 2): # for every pair of consecutive numbers
            for j in range(i + 1, len(l) - 1):
                for k in range(j + 1, len(l)):
                    if l[i] + l[j] + l[k] == 0: # check for triplets
                        c += 1
        return c == 3 # if c = 2, then return False, and if c = 0, then return True
