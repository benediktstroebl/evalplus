```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that takes a list `l` as input and returns a list of all positive numbers found in `l`. The function accomplishes this using a list comprehension and filtering out elements that are not greater than 0. 

To test this function, you can call it with different lists and verify that it returns the expected outputs as documented in the function docstring. 

```python
# Test case 1
input_list = [-1, 2, -4, 5, 6]
expected_output = [2, 5, 6]
result = get_positive(input_list)
assert result == expected_output

# Test case 2
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
expected_output = [5, 3, 2, 3, 9, 123, 1]
result = get_positive(input_list)
assert result == expected_output
``` 

This provides confidence that the function correctly solves the problem and produces the desired results.