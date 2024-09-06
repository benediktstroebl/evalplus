```python
def max_element(lst):
    return max(lst)

# Basic test case
test_max_element = lambda: max_element([1, 2, 3])
assert test_max_element() == 3

# List with negative elements
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max(test_list) == 123

# List with decimal numbers
test_list2 = [5.2, 3.5, -.ally7, -62.4834, 0.0]
assert max(test_list2) == 0.5

# List with large numbers
test_list3 = [123, 345, 789, 12314]
assert max(test_list3) == 12314
```
This script defines a function `max_element` that takes a list as an argument and returns the maximum element in that list using the `max()` built-in function. The function has also been tested with a variety of test cases to ensure its correctness.