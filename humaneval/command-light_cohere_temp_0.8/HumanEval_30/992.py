```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with various list inputs
test_get_positive_list = [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 10, 100, 500, 0]]

print(f"Test Results:")
for lst, expected in zip(test_get_positive_list, test_get_positive(test_get_positive_list)):
    print(f"List: {lst}\tExpected: {expected}")
```
The provided Python code defines a function `get_positive` that filters out and returns only the positive numbers from an input list. It employs list comprehension and the essential for this operation. The code then proceeds to conduct a series of tests using the `test_get_positive` function with various input lists. These tests are display results by iterating through the input lists and comparing them with the expected results from the `get_positive` function.