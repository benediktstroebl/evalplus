

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
    for i in range(len(l)):
        start_index = i + 1
        end_index = len(l) - 1
        while start_index < end_index:
            sum_to_zero = l[i] + l[start_index] + l[end_index]
            if sum_to_zero == 0:
                return True
            elif sum_to_zero < 0:
                start_index += 1
            else:
                end_index -= 1
    return False

