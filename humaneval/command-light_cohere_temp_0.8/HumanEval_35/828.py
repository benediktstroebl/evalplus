```python
def max_element(lst):
    if not_negative(lst):
        return max(lst)
    else:
        raise ValueError("Input list must not contain negative values")

def test_max_element(test_lst):
    try:
        return max_element(test_lst)
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Example usage
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_result = test_max_element(test_data)
if test_result is not None:
    print("Test passed")
else:
    print("Test failed")
```

This script defines a function `max_element` that calculates the maximum element in a list, considering non-negative values. The function also includes a corresponding test function `test_max_element` to verify the correctness of the `max_element` function with a given list. The script then provides an test data and executes the test function.