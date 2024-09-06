```python
def pairs_sum_to_zero(l):
    """
    Check whether the list has two distinct elements that sum up to zero.
    """
    Returns:
        list of integers
    """
    # Check if the list has two distinct elements that sum up to zero
    for i in range(len(l)//2):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 0:
                return False
    return True
```