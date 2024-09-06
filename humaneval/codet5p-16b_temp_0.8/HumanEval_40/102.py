

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

    # the first element in the list needs to be a duplicate
    l.sort()
    for index in range(len(l) - 2):
        if index > 0 and l[index] == l[index-1]:
            continue

        low, high = index+1, len(l) - 1
        while low < high:
            if l[index] + l[low] + l[high] == 0:
                return True
            elif l[index] + l[low] + l[high] > 0:
                high -= 1
            else:
                low += 1
    return False
