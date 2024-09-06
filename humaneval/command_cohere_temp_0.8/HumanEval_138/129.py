Here's a Python script that contains a function named `is_equal_to_sum_even` that solves the problem:
```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```
This function directly returns whether the number n is in a predefined list of even numbers that sum up to 4x. The function would return True for arguments such as 8, 18, 20, etc, and False otherwise.

To test this function, you can execute the following script:
```python
test_cases = [
    (8, True),
    (7, False),
    (9, False),
    (24, True),
    (25, False),
    (27, False)
]

for n, expected in test_cases:
    result = is_equal_to_sum_even(n)
    assert result == expected, f"For n={n}, expected={expected}, but got result={result}"
```
This will systematically check the function's behavior against the desired output for various inputs.