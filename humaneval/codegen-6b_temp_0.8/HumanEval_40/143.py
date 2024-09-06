

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
    sorted_list = sorted(l)
    for i in range(len(sorted_list) - 1):
        first_value = sorted_list[i]
        second_value = sorted_list[i + 1]
        value = abs(first_value - second_value)
        if i != 0:
            if (value + sorted_list[i - 1]) == 0:
                return True
    return False
