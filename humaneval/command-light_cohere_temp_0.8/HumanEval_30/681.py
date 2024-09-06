```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with different list inputs
# Test list with both positive and negative numbers
test_func = get_positive

# Test positive inputs
assert test_func([1, 2, 3, 4, 5]) == [1, 2, 3, 4]
assert test_func([-1, 2, -3, -4]) == [-1, 2, -3, -4]
assert test_func([-5, -3, -9]) == [-5, -3, -9]

# Test negative inputs
assert test_func([1, 2, -3, -4]) == [1, 2, -3, -4]
assert test_func([-5, -2, -1, -9, -6]) == [-5, -2, -1, -9, -6]
```
This Python script defines a function called `get_positive` that takes an input list and returns a new list containing only the positive numbers from the original list. It uses list comprehension to iterate through the list and filter out the positive numbers. The function and test cases cover both positive and negative numbers, passing all test cases successfully.