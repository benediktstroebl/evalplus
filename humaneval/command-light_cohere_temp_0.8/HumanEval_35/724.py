```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = [
    [
        l = [-5, 3, 2, -10, 0, 1],
        max_element(l) == 1,         # Should return 1
        l = [5, 3, -5, 2, -3, 3, 9, 0, 123],
        max_element(l) == 123,     # Should return 123
    ]
]

# Main function
if __name__ == "__main__":
    for test in test_max_element:
        assert max_element(test[1]) == test[2], "Test failed"
```

This Python code defines a function `max_element` within a self-contained module that tests and validates the function's behavior. The function uses the max function to return the maximum element in the list, and the test cases ensure that the function behaves correctly for different lists. The main function runs the region, where it executes the test cases and checks if the function output matches the expected result.