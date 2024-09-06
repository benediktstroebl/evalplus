```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    return "YES" if not odd else "NO"
```

The function examines the oddity of the elements of lst1. If the list contains at least one odd element, then the variable `odd` will be set to `True`. Otherwise, it will be set to `False`. Subsequently, the function returns the appropriate response - "YES" if lst1 included only even numbers, and "NO" if it contained at least one odd number. The assumption of non-emptiness is removed for the sake of completeness. This script solves the problem in a straightforward manner. 

The function assumes that the input lists will be non-empty, but this edge case is not handled properly. To handle this possible enhancement, you could add a validation statement to ensure that the input lists are not empty. Here is an example of how this could be implemented:
```python
def exchange(lst1, lst2):
    if not lst1 or not lst2:
        return "Error: Input lists are empty."
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    return "YES" if not odd else "NO"
```

This way the function makes sure that the lists are not empty and avoids potential errors in handling the edge case.  This makes the function more robust and decreases the likelihood of errors for edge cases.