```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> Test with an list of numbers:
    - [1, 3, 5, 0] is False
    - [1, 3, -2, 1] is True
    - [1, 2, 3, 7] is False
    - [] is False
    - [2, 4, -5, 3, 9, 7] is True
    """
    for el in l:
        if sum(el) < 0:
            return False
    return True
```