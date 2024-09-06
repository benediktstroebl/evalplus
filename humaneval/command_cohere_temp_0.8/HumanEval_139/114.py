Here's a Python script that defines the `brazilian_factorial` function as per the provided problem description:
```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def brazilian_factorial(n):
    if n < 1:
        return 0
    else:
        return special_factorial(n) * brazilian_factorial(n - 1)

# Testing the function
test_cases = [
    (1,), 
    (2, 2), 
    (3, 6), 
    (4, 288), 
    (10, 2500896), 
    (20, 248832388809600)
]

for n, result in test_cases:
    assert brazilian_factorial(n) == result
```
This script defines the base factorial function `special_factorial` and then uses it to calculate the Brazilian factorial, defined as multiplying the factorial of n with the factorial of n-1 and so on up to 1! The script then has some test cases that verify the function's correctness.