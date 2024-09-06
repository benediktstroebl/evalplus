

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

    # sort the list
    l.sort()

    for index, num in enumerate(l):
        if index > 0 and l[index-1] == num:
            continue
        target = -num
        left = index + 1
        right = len(l) - 1
        while left < right:
            if l[left] + l[right] == target:
                return True
            if l[left] + l[right] < target:
                left += 1
            else:
                right -= 1
    return False

