```python
def max_element(lst):
    if not_list(lst):  # Convert list to integer array
        return max(l for l in lst)
    elif len(lst) == 0:
        return None
    else:
        raise ValueError("Input list must be a non-empty list.")

# Unit tests
test_max_element = [
    (None, None),
    ([], None),
    ((5,), None),
    # Add more tests here...
]

for test in test_max_element:
    actual = max_element(test)
    expected = test[1]
    assert actual == expected, f"Test {test}: {actual} != {expected}"
```
This script defines a function max_element that calculates and returns the maximum element in a given list. It includes a test cases with the function, and performs corresponding assertions. The function also checks if the list is empty and raises an error for invalid inputs.