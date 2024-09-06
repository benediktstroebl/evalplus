```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension and the filter out the three elements with sum equal to zero.
    """
Python list comprehension and filtering out the three elements with the same sum:
{x for x in l if sum([x for x in l]) == 0}
    """
return bool(len([x for x in l if sum([x for x in l]) == 0]))
```