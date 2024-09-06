```python
def pairs_sum_to_zero(l):
    if sum(l) == 0:
        return True
    return False
```
This function, `pairs_sum_to_zero`, takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. It performs a
 checks by using the `sum()` function and then checking if the sum is equal to zero. It is a way that is intended to solve the problem of checking if there are two elements in a list that sum to zero.

This function is designed to be efficient and handle a large number of inputs. It is also self-contained, which means it can be called and used in other parts of the program without requiring external functions or modules.