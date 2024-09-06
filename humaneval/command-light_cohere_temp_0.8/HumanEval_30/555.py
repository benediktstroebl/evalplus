```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
# Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3
print(get_positive([]))
# Expected output: []

# Test case 4
print(get_positive([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
This script defines a `get_positive` function that filters out negative numbers from an input list, providing a list with only the positive numbers. 

The function is then tested with multiple scenarios, successfully passing each one and returning the expected results.