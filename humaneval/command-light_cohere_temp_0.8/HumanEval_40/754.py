```python
def triples_sum_to_zero(l: list):
    """
    Function to check if three distinct elements in the list sum to zero.
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
    n = len(l)
    for i in range(n - 2):
        for j in range(i + 1, n):
            total = l[i] + l[j] + l[i + j]
            if total < 0:
                return False
    return True
```