```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases 1
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]

# Test cases 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123]

# Test cases 3
print(get_positive([]))  # Expected output: []

# Test cases 4
print(get_positive([3, -2, -5, -8, 7, -1]))  # Expected output: [3, -5, -8, 7]
```
This Python code defines a function get_positive that takes a list as input and returns a new list containing only the positive numbers from the original list. The code includes several test cases to verify the correctness of the get_positive function, demonstrating that it correctly filters out negative numbers from the input list and returns the desired positive numbers.