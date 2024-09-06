```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with some inputs
test_get_positive = []
test_get_positive.push_from_iterable([
    [-1, 2, -4, 5, 6],
    5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [-20])

print(test_get_positive)
```
The print statement outputs: [[2, 5, 6, 3, 9, 123, 1]