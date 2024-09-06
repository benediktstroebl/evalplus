```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the function with a sample input
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)
``` 
This function `unique` takes a list as an argument and returns a new list containing the unique elements of the original list, which are sorted in ascending order.