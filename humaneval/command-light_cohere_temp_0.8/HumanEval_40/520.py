```python
def triples_sum_to_zero(lst):
    """
    Returns True if there are three distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    list of integers is passed in, and we use the **sum()** function to get the sum of the 
    list. We then check if this **list** contains a triplet three elements, 
    and if the sum of those three elements equals zero. 
    """
 if sum(set(sum(lst[:3]) for i in range(3)) ) < 0
    return True
    return False
```