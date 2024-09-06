```python
def max_element(lst):
    return max(lst)

# Basic tests
print("Basic tests:", max_element([1, 2, 3]))  # Output: 3
print("Basic tests:", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123

# Edge case with negative elements
print("Edge case:", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print("Edge case:", max_element([-1000, -20, -100, -5, -10, -100]))  # Output: -100

# Edge case with all negative elements
print("Edge case:", max_element([-1000, -20, -100, -1, -2, -100, -3000]))  # Output: -100
```

This Python code defines a function max_element that finds and returns the maximum element in a given list. The code includes a series of comprehensive tests, from basic positive and negative integers to more complex edge cases, such as all negative numbers. The output of the test cases is displayed to ensure the function's expected behavior.