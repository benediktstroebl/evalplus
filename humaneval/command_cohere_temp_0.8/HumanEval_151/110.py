Here's a Python script that contains a function named `double_the_difference` designed to solve the specified problem:
```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 != 0 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result
```

This function iterates through each number in the input list. If the number is odd, non-negative, and an integer, its square is added to the `result`. The function returns 0 if the input list is empty.

To demonstrate the functionality, here are some test cases and the expected output:
```python
test_cases = [
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
    ([], 0),
    ([], 0),
]

for input_list, expected in test_cases:
    output = double_the_difference(input_list)
    assert output == expected, f"For input {input_list}, expected {expected}, got {output}"
```

This test suite covers various scenarios, ensuring the function behaves as expected. The function's docstring also provides clear guidance on the problem statement.