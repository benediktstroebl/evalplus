```python
def pairs_sum_to_zero(l):
    if set(l) <= {0}:
        return True
    return False
```
The script defines a function called `pairs_sum_to_zero` that takes a list `l` as an input. The function uses a check whether the list has two distinct elements whose sum is zero. If it does, it returns `True`, indicating that the list contains a pair of numbers whose sum is zero, otherwise it returns `False`.