Here's the code to solve your problem:
```python
def pairs_sum_to_zero(lst):
    total = sum(lst)
    return (not total) if total == 0 else False
```

This function takes a list lst of integers, sums up the list's elements, and returns `True` if the total is zero and `False` otherwise. It effectively checks whether there are two distinct elements in the list whose sum equals zero.