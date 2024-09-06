```python
def pairs_sum_to_zero(lst):
    """
    Checks if there are two distinct elements in the list that sum up to zero.
    Returns: True if there are two such distinct elements, and False otherwise.
    """
    Two distinct elements = lst[:1] + lst[1:]
    for x, y in zip(lst[:-], lst[1:]):
        if x + y == 0:
            return False
    return True
```