```python
def max_element(lst):
    return max(lst)

# Basic test cases
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Corner cases with negative and zero lists
assert max_element([]) == None
assert max_element([-5, -3, 7]) == None
assert max_element([123]) == None

# Edge cases with one element
assert max_element([1, 2, 3]) == 1
assert max_element([-4, -8, 9]) == -8

# Long lists
assert max_element([1, 2, 3, ...]) == 3
assert max_element([0:100, 1, 2, 3]) == 0
```
The function `max_element` computes the maximum element in the provided list.  It also has corner cases, basic test cases, and edge cases to ensure its correctness.