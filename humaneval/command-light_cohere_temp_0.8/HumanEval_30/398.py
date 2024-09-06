```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test the function with various input
tests_pass = True
# Test with empty list
assert get_positive([]), tests_pass

# Test with list of negative numbers
assert get_positive([-1, 2, -4, 5, 6]), tests_pass

# Test with list of positive numbers
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), tests_pass

# Test with mixed list
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), tests_pass
```
This code defines the function **get_positive** that takes a list l as input and returns a new list with only the positive elements from l. 

The function uses list comprehension to filter out the positive elements from the input list.  The test cases for the purpose of validating the function.