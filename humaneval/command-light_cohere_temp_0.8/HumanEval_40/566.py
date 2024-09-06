```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """

    The list must contain exactly three distinct elements.

    If the list must be numeric (int or float).
    """
    if len(l) != 3:
        return False

    sums = [x + y + z for x, y, z in zip(l)]
    return sums == 0
```