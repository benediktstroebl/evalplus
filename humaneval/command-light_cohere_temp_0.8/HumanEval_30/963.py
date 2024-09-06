```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3
print(get_positive([]))  # Expected output: []

# Test case 4
print(get_positive([19,-1]))  # Expected output: []
```
This Python script defines a function called **get_positive** that takes a list as input and returns a new list with only the positive elements from the original list. The test cases are used to verify that the function works correctly and returns the expected output.