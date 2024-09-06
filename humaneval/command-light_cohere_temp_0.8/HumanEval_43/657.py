```python
def pairs_sum_to_zero(l):
    """
    Returns True if all elements in the list sum up to zero, False otherwise.
    """
    takes a list of integers as an input.
    sums = 0
    sum(x * y for x, y in zip(l))
    return sums == 0
```