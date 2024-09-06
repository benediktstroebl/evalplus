```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3 (Negative input)
assert max_element([-5, -3, -7]) == -7

# Test case 4 (List with one element)
assert max_element([9]) == 9
```
The function max_element takes a list lst as input and returns the maximum element in the list. It uses the max() function to find the maximum element. Test cases 1, which use assert statements to verify the correctness of the max_element function with different input lists.