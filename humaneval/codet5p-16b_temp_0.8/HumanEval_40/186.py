

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

    found = False
    for first_number in l:
        for second_number in l:
            for third_number in l:
                if (
                    first_number + second_number + third_number == 0
                    and first_number!= second_number
                    and second_number!= third_number
                    and first_number!= third_number
                ):
                    found = True
                    break
            if found:
                break
        if found:
            break
    return found
