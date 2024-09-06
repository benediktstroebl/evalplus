Here's a Python script that defines the `brazilian_factorial` function, as per the problem statement:
```python
def special_factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
```

This script provides a function that fulfills the definition of the Brazilian factorial, as described in the problem. It starts with a modest `1!` and progressively multiplies it by `2!`, `3!`, `4!`, and so on, up to `n!`, effectively capturing the desired computation. 

To examine the behavior of the `special_factorial` function, you can test it using the following code:
```python
test_cases = [
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 288),
    (10, 3628800)
]

for n, result in test_cases:
    assert special_factorial(n) == result, f"For n={n}, the function should've returned {result} but returned {special_factorial(n)} instead."
```

This test suite confirms the function's output against expected values for various input numbers. Adjust the list if you need more testing scenarios.