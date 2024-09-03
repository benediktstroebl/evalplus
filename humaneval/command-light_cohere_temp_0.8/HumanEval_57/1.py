```python
def monotonic(lst): 
    if sorted(lst) == lst:
        return True
    return False
```  This function will determine whether the list elements are monotonic. It will return True if the monotonic and vice versa.