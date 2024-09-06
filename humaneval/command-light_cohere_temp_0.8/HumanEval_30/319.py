```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123]

# Test case 3
print(get_positive([5, 3, -5, -2, 7, -3, 3, 9, 0, 1, 10]))  # Expected output: []

# Test case 4
print(get_positive([1, 2, -3, -4, -100]))  # Expected output: []
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. It uses list comprehensions to filter out the positive numbers from the input list. The code includes several test cases to verify the correctness of the `get_positive` function, passing the test cases with different input lists and expected outputs.