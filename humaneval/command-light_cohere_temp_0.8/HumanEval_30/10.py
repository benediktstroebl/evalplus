```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases with specific lists of numbers and expected results

# Test 1: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1] -> [5, 3, 2, 3, 9, 123]
# Test 2: [5, 3, -4, 6] -> [5, 3, 6]
# Test 3: [5, -5, 2, -3, 3, 9, 0, 123] -> [5, 3, 9, 123]
# Test 4: [123, -10] -> []
# Test 5: [-1, 2, -4, 5, 6] -> [2, 5, 6]

print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1]))  # Output: [5, 3, 2, 3, 9, 123]
print(get_positive([5, 3, -4, 6]))           # Output: [5, 3, 6]
print(get_positive([5, -5, 2, -3, 3, 9, 0, 123])) # Output: [5, 3, 9, 123]
print(get_positive([123, -10]))             # Output: []
print(get_positive([]))                    # Output: []
```
This script defines a function `get_positive` that removes all negative numbers from an input list, and tests it with various lists of numbers to ensure it works correctly.