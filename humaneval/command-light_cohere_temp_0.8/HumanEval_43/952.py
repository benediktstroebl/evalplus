```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

test cases are included as examples to ensure the function's correctness.
"""
    return any(x+y > 0 for x,y in zip(l))
```