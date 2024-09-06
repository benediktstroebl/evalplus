```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test cases
test_max_element = [
    "Test array with negative numbers:", [-5, -3, 3],
    "Test array with floating numbers: [0.2, 1. Additionally: a list of numbers is a valid input for max().](el): 123",
    "Test array with outlier numbers: [5, 3, -5, 2, -3, 3, 9, 0, 123],
    "Test array with duplicate elements: [1, 2, 3, 2] (This is valid input)"
]

# Test the function
for text in test_max_element:
    try:
        result = max_element(text.value())
        assert result == eval(f'{text}\n{result}')
        print(f"Test {text} passed")
    except Exception as e:
        print(f"Test {text} failed: {e}")
```
The function max_element returns the largest value in the list. It uses the max function to find the maximum element in the list. The test cases ensure that the function works correctly for different input types.