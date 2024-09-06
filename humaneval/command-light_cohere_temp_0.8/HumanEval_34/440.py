```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    set1 = set(l)
    return list(set1)

# Test the function with markdown code block
test_code = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_code))
``` 
This code defines a function called unique that takes a list l as an argument and returns a new list containing the unique elements from the original list. The set1 elements are then removed from the original list and then converted back to a list. The output of this code block is then [0, 2, 3, 5, 9, 123], which are the unique elements in the test list.