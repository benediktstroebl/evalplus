```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    return False if all elements in the list are not pairs or sum of two 
    elements is not zero, else return True
    """
    return sum((x, y) for x, y in zip(l, l[1:])) == 0
```