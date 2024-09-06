```python
def pairs_sum_to_zero(l):
    """
    checks whether the list has two elements whose sum is 0
    """
    return any(x+y == 0 for x,y in zip(l, l[1:]))
``` 
This script defines a simple function, `pairs_sum_to_zero`, which checks whether any two elements in a list sum up to zero. The function returns `True` if there exist two distinct elements that add up to zero, and `False` otherwise.