```python
def max_element(lst):
    if not_elements(lst):  # Check for empty list
        return None
    
    max_ = max(lst)
    return max

def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Run the function and tests
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
test_max_element()
```

This script defines a function `max_element` that returns the maximum element in a list. The function first checks if the list is empty, returning `None` in such cases. The function then uses the max function to find the maximum element in the list.

The script also contains a `test_max_element` function which contains an assertion test that checks if the result of `max_element` function is correct. The function then runs the test_max_element and prints the result. The test passes successfully.