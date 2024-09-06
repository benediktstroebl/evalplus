```python
def pairs_sum_to_zero(l):
    """
    Check if list of integers sums to zero
    Return: True if all elements sum to zero, False otherwise.
    """
    return sum(x for x in l) == 0
```