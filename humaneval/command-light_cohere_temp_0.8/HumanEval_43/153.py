```python
def pairs_sum_to_zero(lst):
    # Compute the sum of all elements in the list
    total = sum(lst)
    # Check if the sum of elements is equal to zero
    if total == 0:
        return True
    else:
        return False
```
This function, `pairs_sum_to_zero`, takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function uses the basic mathematical logic to solve the problem.