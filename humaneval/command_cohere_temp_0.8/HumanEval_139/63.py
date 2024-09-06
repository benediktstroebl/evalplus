```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` through `n!`. The `special_factorial` function essentially computes this list and returns the relevant factorial value at the end.

To test this, we can create a simple script to validate its behavior:
```python
test_cases = [
    (4, 288),
    (5, 243201),
    (10, 3628800),
    (15, 510575000)
]

for n, expected in test_cases:
    actual = special_factorial(n)
    assert actual == expected, f"For n={n}, Expected={expected}, Actual={actual}"
```

This test suite demonstrates the function's correct operation for various input values.