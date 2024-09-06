```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension:
    The sum of all the elements in the list must be zero to pass the test.
"""
    return sum(x for x in l if x != 0) == 0
```
This function will return True if the list has two distinct elements whose sum is equal to zero, and False otherwise. The function uses a list comprehension to check if the sum of all the elements in the list is equal to zero.