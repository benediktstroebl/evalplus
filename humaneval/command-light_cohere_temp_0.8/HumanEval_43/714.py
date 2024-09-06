```python
def pairs_sum_to_zero(l):
    """
    Function that returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    elements with an list of integers, and sum the two highest integers to get a value less than or equal to zero.
    If the elements an list and sum of the two highest integers will be equal to 0, 
    and the list will have two distinct elements.
    """
return sum(x for x in sorted(l)) < 0
```