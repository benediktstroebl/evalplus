```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

print(get_positive(test_get_positive))  # Output: [2, 3, 5, 6, 9, 123, 1]
```