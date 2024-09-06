```python
def max_element(lst):
    if not_elements(lst):
        return None  # Handle empty list to avoid errors
    return max(lst, key=lambda x: x)

def test_max_element(test_lst):
    expected = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    got = max_element(test_lst)
    assert got == expected, f"Expected: {expected}, Got: {got}"

# Example usage
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element(test_data)
```

This code provides a function `max_element` that calculates the maximum element in a given list, and includes tests to ensure its functionality. The `test_max_element` function tests this `max_element` function with a provided list, and the two values should be equal for the test to pass.

Remember to ensure the code is properly indented and formatted to improve readability and maintain consistent coding styles.