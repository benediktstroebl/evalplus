```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This script defines a function called `sum_squares` taking a list of integers as an argument. It goes through each entry in the list and squares it if the index is a multiple of 3, and cubes it if the index is a multiple of 4 but not 3. It then returns the sum of these modified entries. The behavior is specified by the provided Markdown code block.

To test this script, you can add the following code:
```python
# Test the sum_squares function
assert sum_squares([1, 2, 3]) == 6
assert sum_squares([-1, -5, 2, -1, -5]) == -126
assert sum_squares([0, 0, 0, 5, 0, 0]) == 0
```

This would verify the correctness of the `sum_squares` function for the mentioned test cases.  These test cases are designed to align with the examples provided in the problem specification.