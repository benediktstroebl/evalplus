```python
def pairs_sum_to_zero(l):
    """
    Function that checks whether all pairs of elements in the list sum to zero.
    Returns: True if there are two distinct elements that sum to zero,
    and False otherwise.
    """
    test cases:
    >>> test_pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> test_pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> test_pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> test_pairs_sum_to_zero([1])
    False
    """
    for i in range(len(l) // 2):
        x = l[i] + l[i + 1]
        if x == 0:
            return True
    return False
```
This Python function, `pairs_sum_to_zero`, takes a list `l` as input and checks whether there are two distinct elements that sum to zero in the list. It iterates through two elements in the list and checks if their sum is equal to zero. Then, it returns `True` if there are two such elements that sum to zero, and `False` otherwise.