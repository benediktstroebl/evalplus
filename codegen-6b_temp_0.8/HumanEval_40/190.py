

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
    # your code here
    l2 = l[:]
    l2.sort()

    for i in range(len(l2)-1):
        if l2[i] == 0 or l2[i] == l2[i+1]:
            continue
        left = l2[i]
        right = l2[i+1]
        result = left + right
        left_index = binary_search(l2, left)
        right_index = binary_search(l2, right)
        if left_index != -1 and right_index != -1:
            return True
    return False
