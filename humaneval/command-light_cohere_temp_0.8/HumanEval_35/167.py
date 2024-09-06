```python
def max_element(lst):
    if not_integer(lst) or not isinstance(lst, list):
        raise TypeError("Input must be an integer list.")
    return max(lst)

# Test cases
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

test_non_list = [1, 2, 3]
try:
    max_element(test_non_list)
except TypeError as e:
    assert str(e) == "Input must be an integer list"
```
This script defines a function `max_element` that takes a list as an argument and returns the maximum element in the list. The function also includes test cases to ensure its correctness. The test cases ensure that the function handles different input types correctly and raises the appropriate error if the input is not a valid integer list.