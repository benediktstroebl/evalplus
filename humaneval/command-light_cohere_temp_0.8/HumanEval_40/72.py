Here is a Python script with a self-contained function that solves the problem of checking if there are three distinct elements in a list that sum to zero:
```python
def triples_sum_to_zero(lst):
    return all(sum(x) == 0 for x in lst) and any(x != 0 for x in lst)
```

This script defines a `triples_sum_to_zero` function that takes a list `lst` as input. The function returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise. It uses the `all()` to check if there are three distinct elements in the list that sum to zero, and `any()` to check if there are any elements in the list that are not equal to zero.