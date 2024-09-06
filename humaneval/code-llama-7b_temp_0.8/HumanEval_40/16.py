

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
    seen = set()

    for item in l:
        if item in seen:
            continue
        seen.add(item)

        for item2 in l:
            if item2 in seen:
                continue

            if item == item2:
                continue

            difference = 0 - item - item2

            if difference in seen:
                return True

            seen.add(difference)

    return False

