```python
def pairs_sum_to_zero(l):
    if not set(l) <= {0}:
        return True
    return False
``` 
This code defines a function called pairs_sum_to_zero that takes a list of integers as an input and determines if there are two distinct elements in the list whose sum is equal to zero. 

It utilizes the inequality of sets to check if the set of elements is strictly less than or equal to zero, and if so, it immediately returns True. Otherwise, it returns False. 

This approach efficiently solves the problem of determining if there are pairs of elements in the list whose sum equals zero, using a set-based approach.