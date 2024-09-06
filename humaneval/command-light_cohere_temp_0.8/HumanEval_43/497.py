```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test:
    >>> test = pairs_sum_to_zero([1, 3, 5, 0])
    >>> print(test)
    True
    >>> test = pairs_sum_to_zero([1, 3, -2, 1])
    >>> print(test)
    False
    """
    s = sum(l)
    return (s == 0)
```