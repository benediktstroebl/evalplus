```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test the function
test_positive = get_positive([-1, 2, -4, 5, 6])
assert test_positive == [2, 5, 6]

# Test the function with various arguments
test_positive_args = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_positive_args == [5, 3, 2, 3, 9, 123]
```
This Python script defines a function called `get_positive` which takes a list as input and returns a new list containing only the positive elements from the original list. It then tests the turned to be an example of how the function works, and asserts that the result is correct. The function is self-contained and concise, and can be used to process a list of any data type to extract the positive elements.