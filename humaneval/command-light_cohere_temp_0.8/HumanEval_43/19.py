```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    False otherwise.
    """
    example input:
    [1, 3, 5, 0]
    """
    for pair in l:
        sum(pair)
    return sum(pair) == 0
```