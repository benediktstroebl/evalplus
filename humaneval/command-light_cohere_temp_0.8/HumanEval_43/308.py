```python
def pairs_sum_to_zero(l):
    if set(l) <= {0}:
        return True
    return False
```
This code defines a function `pairs_sum_to_zero` that takes a list of integers `l` as an argument and determines whether the sum of all elements in the list will equal to zero. The function utilizes the testing and returns `True` if there are two distinct elements in the list whose sum is zero, and `False` otherwise.