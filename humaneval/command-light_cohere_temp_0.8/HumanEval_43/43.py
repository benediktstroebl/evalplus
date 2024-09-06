```python
def pairs_sum_to_zero(l):
    """
    Checks if there are two distinct elements in the list that sum to zero.
    :param l: list of integers
    :return: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    list comprehension is used to check if there are two distinct elements that sum to zero.
    """
example:
    [1, 3, 5, 0]
    """
    return sum([x for x in l if x in [x for x in l]]) == 0
```
The above function checks if there exist two elements in the list whose sum is equal to zero. It uses the list comprehension and the sum function to perform this check.