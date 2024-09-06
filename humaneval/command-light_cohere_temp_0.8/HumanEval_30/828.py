```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function
test_positive = get_positive([-1, 2, -4, 5, 6])
print(test_positive)  # Expected output: [2, 5, 6]

test_positive2 = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
print(test_positive2)  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```
This code defines a function `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the original list. The function is tested using two different test cases and the expected outputs are [2, 5, 6] and [5, 3, 2, 3, 9, 123], respectively.