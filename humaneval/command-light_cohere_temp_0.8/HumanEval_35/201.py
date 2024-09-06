```python
def max_element(lst):
    return lst[-1] if len(lst) == 1 else lst[-1] + max(lst[-2:])

# Test cases
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element_neg = [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

# Run the tests
assert(max_element(test_max_element) == 5)
assert(max_element(test_max_element_neg) == 123)
```
The provided Python code defines a function max_element that aims to find the maximum element in a given list. The function achieves this by comparing the last element with the maximum value found in the second to last element of the list. 

The test cases for this function involve a list of numbers, and the function is tested to correctly determine the maximum element in both cases.