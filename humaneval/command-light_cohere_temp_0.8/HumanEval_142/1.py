```python
def sum_squares(lst):
    """
    This function will take a list of integers and return the sum of all square and cube values in the list.
    """
    list must only contain integer entries.
    """
   
    expected output is the sum of all square and cube values, which is -126 for all valid inputs. 
"""
    return sum(x**2 if x % 3 == 0 else x**3 for x in lst)
```