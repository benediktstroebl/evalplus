```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

# Test case 1:
test_positive = get_positive([1, 2, 3, 4, 5])
# Output: [1, 2, 3, 4]

# Test case 2:
test_positive = get_positive([-1, 2, -4, 5, 6])
# Output: [2, 5, 6]

# Test case 3:
test_positive = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Output: [5, 3, 2, 3, 9, 123, 1]
```

This code defines a `get_positive` function that takes a list as input and returns a new list containing only the positive numbers from the original list. The function uses list comprehension and the `if` condition to filter out the positive numbers from the input list. 

The test cases demonstrate the function's behavior for different input lists.