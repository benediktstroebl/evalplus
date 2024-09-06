```python
def pairs_sum_to_zero(l):
    if set(l) == set([x + y for x, y in zip(l)]):
        return True
    else:
        return False
``` 
This function determines whether every element in the provided list pairs adds up to zero.  It returns True if this if there is at least one pair of elements that do not add up to zero, and False otherwise.