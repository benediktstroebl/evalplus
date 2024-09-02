

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

    for idx, num in enumerate(l):
        left = idx + 1
        right = len(l) - 1

        while left < right:
            left_num = l[left]
            right_num = l[right]
            if left_num + right_num == -num:
                return True
            elif left_num + right_num > -num:
                right -= 1
            else:
                left += 1

    return False

