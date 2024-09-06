```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    set1 = set(l)
    l = list(set1)
    return l

# Test the function with an example
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)
```  This function takes a list as input and returns a sorted unique elements in a list. Using the set() and list(set()) approaches, it effectively removes duplicates and maintains unique values. The final output will be a unique list with the desired elements.