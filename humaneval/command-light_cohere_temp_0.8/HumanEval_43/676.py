```python
def pairs_sum_to_zero(l):
    """
    A function that checks whether a list of integers can sum to zero.
    It returns True if theard two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    tests if the can be passed to the function without any additional arguments and 
    should return a boolean value, either True or False.
    """
    return sum(x for x in l) == 0
```