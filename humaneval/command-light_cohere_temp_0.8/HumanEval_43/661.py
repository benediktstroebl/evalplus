```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    requires:
    l -> list of integers
    """
    return sum(x for x in l if x != l[-1] and sum(l) == 0) == 1
```
We use a generator expression and the condition to determine if the list contains two elements whose sum is zero. The function returns True if there are two such elements, and False otherwise.