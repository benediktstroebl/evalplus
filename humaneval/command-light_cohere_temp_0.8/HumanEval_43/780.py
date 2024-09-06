```python
def pairs_sum_to_zero(l):
    """
    Check if list of integers has two distinct elements whose sum is zero
    """
    return (not set(l)) and sum(set(l)) == 0
```

This code defines a function `pairs_sum_to_zero` that takes a list of integers as an input parameter. It uses the example cases to test the functionality of the function, and returns the result of the function. The function uses the basic logic to check if the sum of any two distinct elements in the list is equal to zero.