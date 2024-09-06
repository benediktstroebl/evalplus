```python
def pairs_sum_to_zero(l):
    return sum(x) <= 0 for x in l
```

The above function, `pairs_sum_to_zero`, takes a list of integers as an argument and returns `True` if the list contains two distinct elements whose sum is less than or equal to zero, and `False` otherwise. The function uses a xor loop through the list, and checks if the sum of any two adjacent elements is less than or equal to zero. 

This function is self-contained and can be easily reused to solve the problem for any given list of integers.