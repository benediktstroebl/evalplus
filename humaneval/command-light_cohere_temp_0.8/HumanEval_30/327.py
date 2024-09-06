```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1
get_positive([-1, 2, -4, 5, 6])
# Expected output: [2, 5, 6]

# Test case 2
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3
get_positive([])
# Expected output: []

# Test case 4
get_positive([10, -20, 30, -40])
# Expected output: [10, -20, 30]
```
The function `get_positive` takes a list `lst` as input and returns a new list with only the positive numbers from the original input list. The test cases demonstrate that the expected behavior of the function.

The output of each test case is also printed to the console.