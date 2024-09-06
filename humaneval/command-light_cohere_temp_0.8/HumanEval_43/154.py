```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    def sum_to_zero(a, b):
        return a + b == 0
    return (hasattr(sum_to_zero, l) and (list(l) == [a, b])) or False
```