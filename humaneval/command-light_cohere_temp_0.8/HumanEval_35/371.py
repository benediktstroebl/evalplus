```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst, default=float('-inf'))

# Test cases
test_max_element = [
    lst=[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    expect=123
]

def test_function(test_case):
    for item in test_case:
        assert max_element(item) == expect, f"Failed at {item}."

test_max_element
```
This script defines a function `max_element` that calculates the maximum element in a given list. The test cases ensure that the function correctly finds the maximum element by comparing its output with expected results. 

The test cases use the `assert` statement to verify the correctness of the `max_element` function with different input lists.