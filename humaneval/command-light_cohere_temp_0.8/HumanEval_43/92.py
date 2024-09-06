```python
def pairs_sum_to_zero(l):
    """
    Function that returns True if there are two distinct elements in the list that sum to zero, and False otherwise.
    """
    list comprehension is a simple test by summing the two most-significant elements and checking if they are equal:
    for i in range(1, len(l)):
        if l[i] + l[i - 1] == 0:
            return False
    return True
```