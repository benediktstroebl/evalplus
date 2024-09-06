```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
The sum of two distinct elements is guaranteed to be zero or negative depending on their order.
    """
    pairs_sum_to_zero([1, 3, 5, 0])
    True
    """
    return (not l[0] + l[1]) == 0
```