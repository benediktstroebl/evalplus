```python
def pairs_sum_to_zero(l):
    """
    Checks if all the elements in the list sum up to zero.
    return True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
l = list(range(0, 6))
    sum = sum(l)
    return sum == 0
```