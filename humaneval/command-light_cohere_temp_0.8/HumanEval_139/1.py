```python
def special_factorial(n):
    """
    The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1). factorial_
    where n > 0
    """
    if n <= 0:
        raise ValueError("Factorial is defined for positive numbers")
    else:
        return n*(n+1)*(n+2)...*1

# Unit tests
assert special_factorial(0) == 1
assert special_factorial(1) == 1
assert special_factorial(2) == 2
assert special_factorial(3) == 6
assert special_factorial(4) == 24
assert special_factorial(5) == 120
assert special_factorial(6) == 720
assert special_factorial(7) == 5040
assert special_factorial(8) == 40320
assert special_factorial(9) == 3628800
```