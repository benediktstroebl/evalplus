

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
    if not l:
        return False
    l_ = l.copy()
    l_.sort()

    for first_index, first_element in enumerate(l_[:-2]):
        for second_index in range(first_index + 1, len(l_) - 1):
            for third_index in range(second_index + 1, len(l_)):
                second_element = l_[second_index]
                third_element = l_[third_index]
                if first_element + second_element + third_element == 0:
                    return True
    return False

