```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension and the elements in the list with the condition sum(element1, element2) < 0, then return True 
    """
    return any(sum(a,b) < 0 for a,b in zip(l))
``` 
The function uses a list comprehension to check if any of the sums of pairs in the list are less than zero.