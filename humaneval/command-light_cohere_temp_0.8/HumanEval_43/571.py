```python
def pairs_sum_to_zero(lst):
    """
    Checks whether all pairs of elements in the list sum to zero.
    Return True if all elements in the list sum to zero, and False otherwise.
    """
    example usage:
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    """
    sum = 0
    for i in range(len(lst) // 2):
        sum += lst[i] + lst[i + 1]
    return sum == 0
```