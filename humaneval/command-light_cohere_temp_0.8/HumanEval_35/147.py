```python
def max_element(lst):
    if not_is_list(lst):
        return max(lst)
    else:
        raise ValueError("Input must be a list")

def test_max_element():
    try:
        result = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        print("Maximum element:", result)
    except ValueError as e:
        print("Error:", str(e))

# Test the function with various inputs
test_max_element()
```
The above Python script defines a function `max_element` that calculates and returns the maximum element from a given list. The `test_max_element` function contains the main test case for this function.  It also includes a handling of potential errors and provides informative output for better code readability.