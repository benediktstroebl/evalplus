```python
def median(lst):
    """Return the median of the list"""
    if len(lst) < 3:
        raise ValueError("List must have at least 3 elements")
    if len(lst) == 3:
        return (lst[0] + lst[1]) / 2.0
   
   
    
    mid1 = (lst[0] + lst[1]) / 2.0
   
   
   
    mid2 = (lst[1] + lst[2]) / 2.0
   
   
   
    return (mid1 + mid2) / 2.0
```
This function calculates the median of the elements in a list. It handles the edge case of the list having less than three elements and raises a `ValueError`, and handles the case where the list has exactly three elements by returning the average of the first two elements.