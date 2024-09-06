```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test cases are provided for as well.

"""

    # List comprehension to filter pairs with sum to zero
    return sum([x+y for x,y in zip(l)]) == 0
```