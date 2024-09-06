```python
def pairs_sum_to_zero(l):
    """
    Function to determine if there are two distinct elements in a list that sum to zero.
    Returns: True if there are two such distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    list of integers contains two numbers that add up to zero, in which case the 
    function returns True; otherwise, False is returned.
    """
return sum(x for x in l) == 0
```