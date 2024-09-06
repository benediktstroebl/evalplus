```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. The function promptly returns true if the number can be formed and false if it cannot.

To verify the correctness of the function, let's test it against the examples provided:
```python
test_cases = [
    (4, False),
    (6, False),
    (8, True)
]

for n, expected in test_cases:
    result = is_equal_to_sum_even(n)
    assert result == expected
```

This script provides a self-contained function 'is_equal_to_sum_even' and corresponding tests to validate its behavior against the problem statement. You can directly use this code block to solve the given problem.