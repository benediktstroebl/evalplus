```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension with a built-in sum function is used to find the sum of the list's elements.

Return:
bool
    """
    return any([sum(x) < 0 for x in l])
```