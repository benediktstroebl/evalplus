```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list of distinct numbers should be easy to write!
    """
    # Use the operator "and" to check if any elements in the list are the sum of two other elements
    # If yes, then it is not possible to have two elements that sum to zero
    # If not, return True
    return any(x==y for x,y in zip(l,l))
```