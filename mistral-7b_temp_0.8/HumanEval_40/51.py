

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

    l.sort()
    if len(l) < 3:
        return False
    if l[0] + l[1] + l[-1] == 0:
        return True

    start_ind = 0
    end_ind = len(l) - 1
    while start_ind < end_ind:
        current_sum = l[start_ind] + l[end_ind]
        if current_sum == 0:
            return True
        elif current_sum > 0:
            end_ind -= 1
        else:
            start_ind += 1

    return False

