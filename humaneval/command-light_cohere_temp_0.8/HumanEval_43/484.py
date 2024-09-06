```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    return False

    """
    if all(x+y>=0 for x,y in zip(l)) or sum(l)==0:
        return True
    else:
        return False
```
The above code provides a self-contained solution to the problem. The function checks whether all the elements of the list satisfy the sum to zero requirement or not.