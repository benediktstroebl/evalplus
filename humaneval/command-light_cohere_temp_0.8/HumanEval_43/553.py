```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    False otherwise.
    """
    test cases are provided in the docstring.
 pairs_sum_to_zero([1, 3, -2, 1])  # returns False
{' 2, 4, -5, 3, 5, 7 }  # returns True
```
The function checks whether there exist two elements that add up to zero. If there are such would any two distinct elements in the list that sum to zero, the function returns True; otherwise, False.

It uses a simple and straightforward approach that iterates through the list and checks if there are two elements with opposite signs that add up to zero.