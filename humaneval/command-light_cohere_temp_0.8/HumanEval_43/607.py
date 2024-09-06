Here is a Python script that defines a function called `pairs_sum_to_zero` solving the problem:
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension is a simple way to find two elements with sum = 0:
    """
    for x, y in l:
        if x + y == 0:
            return True
    return False
```
The above function takes a list `l` as an argument and returns `True` if there are two distinct elements in the list that have sum to zero, and `False` otherwise. The list comprehension is a most efficient way to find such elements.