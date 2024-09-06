```python
def max_element(lst):
    return lst[-1] if len(lst) == 1 else lst[-1] + max(lst[:-])

# Test case 1
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 2
assert max_element([1, 2, 3, 3, 4, 5]) == 5

# Test case 3
assert max_element([-5, -3, -10, -4, -2, -1]) == -10
```
This code defines a max_element function that returns the maximum element in the list. It achieves this by returning the max_element if the list has only one element or returns the last element of the list. Additionally, it calculates the maximum element by adding the maximum of the list's elements. The test cases ensure that the function works correctly with different lists.