```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with a list of numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(test_list)
assert len(result) == 7  # Assertion to check the length is as expected
assert result == [5, 3, 2, 3, 9, 123, 1]  # Assertion to check the correct output
```

This script defines a function `get_positive` that takes a list as an argument and returns a new list containing only the positive integers from the original list. The function is then passed to the test_list and the result is compared with the expected output to ensure the correctness of the function.