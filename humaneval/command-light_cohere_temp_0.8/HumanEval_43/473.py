Here's the improved code:
```python
def pairs_sum_to_zero(lst):
    """
    Returns True if the list has two distinct elements that sum to zero, 
    and False otherwise.
    """
    requires the  a list of integers
    """
    for i in range(1, len(lst)):
        sum_of_two = lst[i-1] + lst[i]
        if sum_of_two == 0:
            return True
    return False
```