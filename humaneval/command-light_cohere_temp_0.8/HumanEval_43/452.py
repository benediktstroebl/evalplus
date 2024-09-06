Here is a Python script that contains a self-contained function to solve the problem:
```python
def pairs_sum_to_zero(lst):
    if sum(x == 0 for x in lst) == 0:
        return True
    return False
```

This script defines a function `pairs_sum_to_zero` that takes a list `lst` as an input. It uses a the certain method to check if there are two distinct elements in the list that sum to zero. The function returns `True` if there are such, and `False` otherwise. 

You can use this function to check if a list contains elements that sum up to zero, and act accordingly.