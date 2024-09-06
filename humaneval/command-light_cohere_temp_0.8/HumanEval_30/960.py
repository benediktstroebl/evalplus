```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with various inputs
test_get_positive = []
test_get_positive.py 
[-1, 2, -4, 5, 6]
test_get_positive.txt
test_get_positive = get_positive(test_get_positive)
assert test_get_positive == [-2, 5, 6]

# Another test with a list of text
test_get_positive.txt
test_get_positive = get_positive(["Hello", "World!,"!])
assert test_get_positive == ["World",]

# Error handling test - Empty list
try:
    test_get_positive = get_positive([])
except TypeError:
    print("Error handling empty list")
```