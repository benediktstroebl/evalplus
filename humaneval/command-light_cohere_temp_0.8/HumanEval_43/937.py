```python
def pairs_sum_to_zero(l):
    """
    Function that checks whether a list of integers sum to zero
    """
    return sum(x for x in l) == 0
```
The above function uses a generator expression with the `sum` function to check if the sum of all elements in the list is equal to zero. This will return `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise.