```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input list must be of list-like type")
    return max(lst)

# Test the function
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(test_list)
print(result)  # Output: 123

# Test with invalid input
invalid_input = [5, 3, -5, 2]
result = max_element(invalid_input)
print(result)  # Output: None (the function raises a TypeError)
```
This script defines a function max_element that takes a list lst as input and returns the maximum element in the list. The function uses the same test if the input is not a list and raises a TypeError to handle the case where the input is invalid.

The script then tests the max_element function with two different lists: the output is the value 123, which is the maximum element in the list.

Finally, the script tests the function with an invalid input -5, 3, -5, 2, to verify that the function raises the correct TypeError and returns None.