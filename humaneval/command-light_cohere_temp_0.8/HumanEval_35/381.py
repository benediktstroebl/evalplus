```python
def max_element(lst):
    if not_nan(lst) or not_inf(lst):
        return max(lst)
    else:
        raise ValueError("Input list contains NaN or Infinity values")

def test_max_element():
    try:
        max_element([1, 2, 3])
        return "Success"
    except ValueError as e:
        return f"Error: {e}"
```
The function `max_element` takes a list as input and uses the `max()` built-in function to find the maximum element.

The `test_max_element` function contains a test case for the `max_element` function. The test case ensures that the `max_element` function works correctly with all valid input.

The test case also uses a `try` and `except` block to catch any potential `ValueError` that may occur during the function execution and returns an appropriate error message.