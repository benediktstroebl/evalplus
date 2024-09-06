```python
def max_element(lst):
    return max(lst)

# Test case 1: Basic list with positive and negative numbers
assert max_element([1, 2, 3]) == 3

# Test case 2: List with decimal numbers
assert max_element([5.2, 3, -1.5, -3, 9.0]) == 9.9


# Test case 3: List with duplicate elements
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 4: Empty list
assert max_element([]):
  assert False

```
The function max_element returns the maximum element in the list. It takes advantage of Python's built-in function max() to achieve this. You can add more test cases to further test the function.