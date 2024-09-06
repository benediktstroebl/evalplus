```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with various lists of numbers
test_get_positive = []
test_get_positive.py  # - [-1, 2, -4, 5, 6]
test_get_positive.py  # [ [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

# Function call
result = get_positive(test_get_positive)

print(result)
```