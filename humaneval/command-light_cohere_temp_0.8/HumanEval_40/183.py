```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> test_sum_to_zero([1, 3, -2, 1])
    True

    >>> test_sum_to_zero([1, 3, -2, 1])
    True

    >>> test_sum_to_zero([1, 2, 3, 7])
    False

    >>> test_sum_to_zero([2, 4, -5, 3, 9, 7])
    True

    >>> test_sum_to_zero([1])
    False
    """
    return sum([x for x in l]) % 3 == 0
```