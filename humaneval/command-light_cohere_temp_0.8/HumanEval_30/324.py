```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
test_get_positive = [
    pytest.TestCase('[-1, 2, -4, 5, 6]', '[2, 5, 6]')
    pytest.TestCase([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    pytest.TestCase([5, -100])  # Another negative number
    ]

# Function main usage
if __name__ == "__main__":
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
```
This Python code defines a function called `get_positive` that filters out negative numbers from an input list, resulting in a new list containing only the positive numbers. It utilizes theessential test suite of tests using `pytest.TestCase` to verify the test if the `get_positive` function successfully removes negative numbers from various input lists. The `main` block ensures the code execution only when the script is run directly (not imported), and it uses the `assert` assertion to validate the function's output for the test cases.