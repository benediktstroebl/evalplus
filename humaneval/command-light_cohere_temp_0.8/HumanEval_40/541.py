```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """

    # Sort the list
    l.sort(key=lambda x: x)

    # Find three distinct elements that sum to zero
    for x, y, z in zip(l, l, l):
        if x + y + z == 0:
            return True
        if x == y and z == -1:
            return True

    return False
```