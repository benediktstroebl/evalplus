```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test cases:
    >>> test_pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> test_pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> test_pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> test_pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> test_pairs_sum_to_zero([1])
    False
    """
    return (not l or sum(l) == 0)
```