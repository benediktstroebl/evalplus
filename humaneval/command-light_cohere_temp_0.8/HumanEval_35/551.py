```python
def max_element(lst):
    return max(lst)

# Test case 1: Basic list with positive and negative numbers
assert max_element([1, 2, 3]) == 3

# Test case 2: List with negative integer as maximum element
assert max_element([5, -5, 2, -3, 3, 9, 0, 123]) == 123

# Test case 3: List with floating numbers
assert max_element([5.2, 3. D, -5, .5, .1]) <= 5.1

# Test case 4: List containing just one element
assert max_element([1]) == 1
```