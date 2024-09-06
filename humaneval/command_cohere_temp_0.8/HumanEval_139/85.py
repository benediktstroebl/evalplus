Here's a Python script that defines the `brazilian_factorial` function as described:
```python
def special_factorial(n):
    product = 1
    for i in range(2, n + 1):
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

for n, expected in test_cases:
    computed = brazilian_factorial(n)
    assert computed == expected, f"For n={n}, Expected={expected}, Computed={computed}"
```

This script defines the `special_factorial` function, which is a simpler expression of the ' Brazilian factorial', where `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!`.

Then, the `brazilian_factorial` function is defined, which calls itself recursively for `n >= 2`, and returns 1 for `n < 2`.

The section tests the function against a list of test cases, computing the `brazilian_factorial` of given input values and comparing the results to expected output.

The assert statement checks if the computed result matches the expected result for each test case, and it fails if they don't match, providing a clear error message. 

This way, the function is tested against various inputs to ensure it behaves as expected. 

To see the code with the included tests, verify the following:
```python
def special_factorial(n):
    product = 1
    for i in range(2, n + 1):
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

for n, expected in test_cases:
    computed = brazilian_factorial(n)
    assert computed == expected, f"For n={n}, Expected={expected}, Computed={computed}"
``` 

This is the most common practice in software development, as it provides clear feedback on how inputs and outputs behave, and it ensures your code behaves as expected across a range of scenarios. 

Let me know if you need anything else!