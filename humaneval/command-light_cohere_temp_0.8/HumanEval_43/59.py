```python
def pairs_sum_to_zero(l):
    """
    returns True if there are two distinct elements in the list that sum to zero, 
    False otherwise.
    """
    elements that two elements in the list with the sum equal to zero:
        -1, -5
        0, -8
        -2, 2
        5, 1
        2, 4
    """
    for x, y in l:
        if x + y == 0:
            return True
    return False
```