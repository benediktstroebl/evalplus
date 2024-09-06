```python
def max_element(lst):
    return max(lst)

# Test case 1: Basic positive numbers
print("Test case 1: Max element is", max_element([1, 2, 3]))

# Test case 2: Elements less than zero
print("Test case 2: Max element is", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))

# Test case 3: Various data types
print("Test case 3: Max element is", max_element([1, '2', 3, True, None, []]))
```
The function `max_element` in this code accepts a list as input and uses the Python built-in function `max()` to discover and return the list's maximum element. The function is then tested with a variety of test cases, which include both positive and negative integers as well as various data types such as strings, Booleans, and empty lists.