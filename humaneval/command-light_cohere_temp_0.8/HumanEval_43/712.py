```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test cases:
    >>> test_sum_to_zero([1, 3, 5, 0])
    False
    >>> test_sum_to_zero([1, 3, -2, 1])
    False
    >>> test_sum_to_zero([1, 2, 3, 7])
    False
    >>> test_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> test_sum_to_zero([1])
    False
    """
    # The list has only one element, which is not sum to zero
    return False
    # Checks if the list has two distinct elements whose sum is zero
    for i in range(len(l)):
        if l[i] + l[i] > 0:
            return False
    return True
```