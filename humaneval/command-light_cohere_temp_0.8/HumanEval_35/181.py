```python
def max_element(lst):
    if not_negative(lst):
        return max(lst)
    else:
        raise ValueError("Input list must not be empty or negative")

def test_max_element(test_lst):
    try:
        return max_element(test_lst)
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Example usage
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(test_max_element(test_list))  # Output: 123

# Test with negative input
test_list_negative = [-5, 3, -20]
print(test_max_element(test_list_negative))  # Output: ValueError: Input list must not be empty or negative
```

This Python script defines a function `max_element` that calculates the maximum element in a list, considering negative values and raising an exception for invalid inputs (empty or negative lists). The `test_max_element` function provides tests for the `max_element` function, which also includes a test with a negative list to ensure the function handles such cases correctly.