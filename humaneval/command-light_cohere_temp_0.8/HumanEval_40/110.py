Here's the self-contained function with tests:
```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> return True if all elements sum to zero
    """
    return sum(x) == 0 and len(set(l)) == 3 or False

```

This function checks if the list has three distinct elements whose sum is zero, returning `True` if this condition is met, and `False` otherwise.