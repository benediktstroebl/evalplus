```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function
test_get_positive = []
test_get_positive.py  = [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [1, 2, 3, 4, 5]]
print(get_positive(test_get_positive))  # Output: [2, 3, 2, 3, 9, 123, 1]
```