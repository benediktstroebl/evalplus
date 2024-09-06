```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with several lists of numbers
# Returns True if all tests pass
test_positive = lambda: all(get_positive([1, -1, 2, 3, -4, 5, 6])) and all(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))

print("Test results:", test_positive())
 ```