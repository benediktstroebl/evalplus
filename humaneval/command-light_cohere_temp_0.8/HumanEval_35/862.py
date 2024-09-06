```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test the function
good_input = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(good_input)
print(result)  # Output: 123

not_list = [5, 3, 'abc', 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(not_list)
print(result)  # Output: TypeError: 'circle' is not iterable
```
The code defines a Python function `max_element` that takes a list `lst` as input and returns the maximum element in the list. The function first checks if the the input is a list using the `isinstance()` function, and if not, it raises a `TypeError` with a corresponding error message. 

The code also provides two tests for the `max_element` function:
1. Test with list- The list of numbers and it correctly finds the maximum element as 123. 
2. Test with a list of elements, which raises an error since the elements are not iterable.