```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list containing both positive and negative numbers
tests = [
    "get_positive([-1, 2, -4, 5, 6]) should return [2, 5, 6]"
    "get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) should return [5, 3, 2, 3, 9, 123, 1]"
]
```