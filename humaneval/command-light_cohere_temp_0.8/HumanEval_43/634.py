```python
def pairs_sum_to_zero(l):
    """
    Function to check if a list of integers can sum to zero.
    """
   
    Returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
List must not be empty.
    """
Two element sum to zero: 1+3 = 4 and -2+1 = -1
    """
    return sum([x for x in l if x in (4, -1)]) == 0
```