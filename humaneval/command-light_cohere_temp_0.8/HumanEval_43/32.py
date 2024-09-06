```python
def pairs_sum_to_zero(l):
    """
    returns True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    list of integers"""
    # Using a set to keep track of the current sum and element
    current_sum = 0
    for num in l:
        current_sum += num
    if current_sum == 0:
        return True
    return False
```