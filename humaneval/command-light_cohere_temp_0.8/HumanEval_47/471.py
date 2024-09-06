```python
def median(lst):
    """Return median of elements in the list lst."""
    # Sort the list in ascending order
    lst.sort()
   
    sort(key=lambda x: x)
    # Calculate middle index
    m = len(lst) // 2
    if len(lst) % 2 == 1:
        return (lst[m])
    else:
        return (lst[m-1] + lst[m]) / 2
```  This function takes a list as input and returns the median of its elements.  It sorts the=l by default, using the sort() method with a lambda function as the key.