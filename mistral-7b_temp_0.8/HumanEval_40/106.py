

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
    #if len(l) < 3:
    #    return False
    #if l.count(0) > 0:
    #    return True

    def does_triple_sum(l):
        i = 0
        j = 1
        k = len(l) - 1
        while i < len(l) and j < len(l) and k > i:
            if l[i] + l[j] + l[k] == 0:
                return True
            i += 1
            j += 1
            k -= 1

        return False


    return does_triple_sum(l)

