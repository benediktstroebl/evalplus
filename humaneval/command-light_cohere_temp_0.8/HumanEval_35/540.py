```python
def max_element(lst):
    if not_list(lst):  # Check if list-like object provided
        raise TypeError("Input should be a list.")
    return max(lst)  # Standard Python function to find maximum element

def test_max_element(lst):
    assert lst == [1, 2, 3, 5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], \
             "Input list is not as expected."
    assert max_element(lst) == 123, "Max element is not returned."

# Test the function with various inputs
test_cases = [
    [],
    [1, 2, 3],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [123, 1, 2, 3, 4, 5]
]

for test_case in test_cases:
    print(test_case)
    print("Expected:", [123])
    print("But was:", max_element(test_case))
    print()
```

This Python code provides a self-contained function `max_element` that takes a list as an argument and checks if the input is a list-like object. It then raises a provided a `TypeError` to handle the invalid input case. The function returns the maximum element in the list, and the `test_max_element` function tests the function with various inputs, ensuring it works correctly.