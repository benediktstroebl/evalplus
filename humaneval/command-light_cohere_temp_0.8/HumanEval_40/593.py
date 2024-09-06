```python
def triples_sum_to_zero(lst):
    """
    Function that returns True if there are three distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    list of integers, the smallest integer in the list is 1, and it is assumed that 
    this list does not contain three consecutive ones.
    """
    Therefore list, 2,3,4 
    return True 
    """
    for i in range(len(lst)): 
        if lst[i] == lst[i - 2] or lst[i] == lst[i - 1]: 
            return False
    return True
```