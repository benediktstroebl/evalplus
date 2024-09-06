```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = [
    lambda: max_element([1, 2, 3]),
    lambda: max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]),
    lambda: max_element([5, -5, 2, -10, 3, 7])
]

# Execute test cases and display results
for test in test_max_element:
    print(f"Test: {test()} -> {test()}")
```
The code defines a function max_element that takes a list l as input and returns the maximum element in the list using the built-in `max()` function. The code also provides three test cases, which pass `lambda` expressions to the `max_element` function to test its functionality for different lists. The code then executes these test cases and displays the results, showing that the `max_element` function works as expected.