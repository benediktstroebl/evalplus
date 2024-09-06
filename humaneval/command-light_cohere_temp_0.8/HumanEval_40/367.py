```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list of integers is not sorted.
    """
    list comprehension is used to filter elements that do not create a valid triplet sum to zero.

Returns: boolean value"""
if sum(map(lambda x: abs(x), l)) == 0:
    return True
else:
    return False
```