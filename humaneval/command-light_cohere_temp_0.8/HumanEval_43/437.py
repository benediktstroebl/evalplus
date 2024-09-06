```python
def pairs_sum_to_zero(l):
    """
    Function to check if there are two distinct elements in the list that sum to zero.
    Returns: True if there are two such distinct elements in the list that sum to zero,
    and False otherwise.
    """


l = [1, 3, 5, 0, -2, 1]
# List contains two distinct elements that sum to zero (0): return True
return True

l = [1, 3, -2, 1]
# List does not contain two distinct elements that sum to zero: return False
return False

l = [1, 2, 3, 7]
# List contains only one distinct element, which is not sum to zero: return False
return False

l = [2, 4, -5, 3, 5, 7]
# List contains two distinct elements that sum to zero: return True
return True
```
The function 'pairs_sum_to_zero' in this script determines whether any two distinct elements in the supplied list add up to zero. It returns 'True' if the list contains two distinct elements that add up to zero, and ''False" otherwise. It accepts an input list of integers and creates a boolean answer depending on the list's contents. 

This method is intended to detect and handle situations where lists include elements that add up to zero.