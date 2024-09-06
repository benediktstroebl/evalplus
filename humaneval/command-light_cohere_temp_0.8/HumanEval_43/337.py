```python
def pairs_sum_to_zero(l):
    """
    Check if all elements in the list sum up to zero
    Returns: True if there are two distinct elements that sum to zero, 
    False otherwise.
    """
    note: The input list is modified.
    """
    test case:
    Test with a list with all positive integers. 
    Should return False.
    """ example: 
    [1, 3, 5, 0]
    """
    for i in range(len(l)):
        l[i] = l[i] + l[i]
    return True
```