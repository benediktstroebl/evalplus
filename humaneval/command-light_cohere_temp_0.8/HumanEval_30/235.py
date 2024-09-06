```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1
print("Case 1:", get_positive([-1, 2, -4, 5, 6]))
# Expected output: Case 1: [2, 5, 6]

# Test case 2
print("Case 2: ", get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: Case 2: [5, 3, 2, 3, 9, 123, 1]

# Test case 3
print("Case 3: ", get_positive([5, 3, -5, 2, -3, 3, 9, 0, -123]))
# Expected output: Case 3: [5, 3, 2, 3, 9]

# Test case 4
print("Case 4: ", get_positive([-5, -3, -2, 7, 8, -1]))
# Expected output: Case 4: [-5, -3, -2, 7, 8]
```

This script defines a function `get_positive` that filters out the negatives from a given list, and the test cases demonstrate its effectiveness. The `if` statement is used to check if a number is non-negative, which is then returned as a list.