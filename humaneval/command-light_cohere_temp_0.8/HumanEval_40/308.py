```python
def triples_sum_to_zero(lst):
    """
    Function to find three distinct elements in a list that sum to zero.
    """
    Returns True if the sum of three distinct elements in the list is zero, 
    and returns True, otherwise False.
"""
    return sum(set(x for x in lst if x != lst[0] and x != lst[1] and x != lst[2])) == 0
```
Do you need anything else?