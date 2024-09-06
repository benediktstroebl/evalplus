```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

"""
    Two elements sum to zero if and only if they are equal and of opposite signs, 
    i.e., either both are positive or both negative. 

    for the particular element is handled as a special case.

# Check if the list contains at least one positive number.
# Initialize two variables to false.
are list contains at least one positive number, return False

# Initialize two variables to True, 

# and loop through list
#
    for x in l:
        if x < 0:
        # if x is negative, set negative flag to False and break out of loop
        else:
            # if x is positive, set positive flag to True and break out of loop
            pass
    if (positive_flag == True) and (negative_flag == False):
        return True
    else:
        return False
```
The function will return True if there are two distinct elements in the list that sum to zero.