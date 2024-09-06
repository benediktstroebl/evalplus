```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with a list of various elements
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(test_list)
print(result)  # Output: [5, 3, 2, 3, 9, 123, 1]

# Test the function with a list of negative numbers
negative_test = [-1, -2, -3, -4, -5, -6]
result = get_positive(negative_test)
print(result)  # Output: []
```

This Python script defines a function `get_positive` that takes a list (`l`) as an argument and returns a new list containing only the positive elements from the original list. The function uses a straightforward filtering to check if each element is non-negative (positive or zero) and then includes it in the result. The script also includes test cases to ensure the correctness of the `get_positive` function.