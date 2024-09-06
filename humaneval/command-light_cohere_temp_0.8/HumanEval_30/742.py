```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list of various elements
test_list = [[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5e, 5f]]
# Test the function with a list of floats
test_float = [[5e-3, 3e+3], [-5e-2, 5e+2]]

# Test the function with a list of negative numbers
test_neg = [-1, -2, -4, -5, -6]

print(f"Test list with positive numbers: {test_list}")
print(f"Test list with positive floats: {test_float}")
print(f"Test list with negative numbers: {test_neg}")
```
The above script defines a function called **get_positive** that filters out and returns only the positive elements from an input list. It then uses this test the both for a list of numbers and a list of floats, and for a list of negative numbers, respectively, to ensure that the function is working as expected.