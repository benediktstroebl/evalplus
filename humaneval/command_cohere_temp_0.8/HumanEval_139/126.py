Here's a Python script that defines the `brazilian_factorial` function as described:
```python
def special_factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def brazilian_factorial(n):
    if n < 2:
        return 1
    else:
        return special_factorial(n) * brazilian_factorial(n - 1)

# Testing the function
test_cases = [
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 288),
    (10, 3628800)
]

for n, answer in test_cases:
    assert brazilian_factorial(n) == answer
```

The `brazilian_factorial` function is defined to recursively calculate the Brazilian factorial of a positive integer `n`. It uses the `special_factorial` function to calculate the factorial of a single number. The test cases are defined to verify the correctness of the implementation against the expected outputs.