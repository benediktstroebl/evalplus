```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    following are a following:
    1. If the sum of the elements is less than 0, return True
    2. If the list is empty, return False
    3. If there are more than 3 elements and they don't sum to zero, return False
    4. If there are exactly three elements and they sum to zero, return True
    """
    if sum(l) < 0:
        return True
    elif len(l) == 0:
        return False
    else:
        return sum(l) == 0
```