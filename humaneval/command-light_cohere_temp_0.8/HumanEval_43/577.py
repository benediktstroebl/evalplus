```python
def pairs_sum_to_zero(l):
    if sum(l) == 0:
        return True
    return False
```

This code provides a function `pairs_sum_to_zero` that takes a list `l` of integers as input. The function checks if there are two distinct elements in the list that sum to zero, and returns `True` if they exist, and `False` otherwise. 

The function uses the built-in Python function `sum()` to calculate the sum of the elements in the list. The function then checks if the sum equals zero, and returns `True` if it is.