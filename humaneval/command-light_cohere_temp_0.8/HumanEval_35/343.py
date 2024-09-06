```python
def max_element(lst):
    return max(lst)

# Test case 1: Positive integers
assert max_element([1, 2, 3]) == 3

# Test case 2: Negative numbers
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3: Complex values
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
This code defines a function max_element that takes a list lst as input and returns the maximum element from that list using the built-in max() function. The test cases ensure that function works correctly for various types of input lists.