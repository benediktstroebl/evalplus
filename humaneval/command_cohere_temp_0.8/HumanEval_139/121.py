Here's a Python script that defines the `brazilian_factorial` function as per the provided description:
```python
def special_factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def brazilian_factorial(n):
    if n < 1:
        return 0
    else:
        return special_factorial(n) * brazilian_factorial(n - 1)

# Testing the function
test_cases = [
    (1,), 
    (4,), 
    (10,), 
    (24,), 
    (27,), 
    (100,), 
    (512,), 
    (1000,), 
]

for n, expected in test_cases:
    result = brazilian_factorial(n)
    if result == expected:
        print(f"Test case {n} passed - Result is {result}")
    else:
        print(f"Test case {n} failed - Expected {expected}, Actual {result}")
```

This script defines the `special_factorial` function, which is equivalent to the standard factorial function. The `brazilian_factorial` function then builds up the result recursively. The script also includes a list of test cases with expected output to validate the function. Each test case is checked against the expected value, and the script prints out whether it passes or fails.