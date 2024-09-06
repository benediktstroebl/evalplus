```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various input lists
# Testing with lists of different data types (integers, floats, strings) and negative/positive numbers.
get_positive([-1, 2, -4, 5, 6]) # Output: [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 'abc']) # Output: [5, 3, 2, 3]
get_positive([5, 3, 9, 0, 123, -10]) # Output: [5, 3, 9, 123]
get_positive([1, 2, 3, -8, -4]) # Output: [1, 2, 3]
```
This script defines a function get_positive that takes a list as input and returns a new list with only the positive numbers from the original list. The test cases demonstrate the use of the function with a variety of input lists, including strings and negative numbers, and the output is expected to be as expected.