```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of a or b must be a positive integer.")
    while a != 1 or b != 1:
        if a % b == 0:
            return b
        a, b = b, a + b
    return

# Test case: positive integers
test_gcd(3, 5)
test_gcd(25, 15)
test_gcd(9, 3)
test_gcd(20, 4)
test_gcd(21, 7)

# Test case: negative numbers
test_gcd(-3, 5)
test_gcd(-25, -15)
test_gcd(-9, -3)
test_gcd(-20, -4)

# Test case: floating-point numbers
test_gcd(3.14, 5)
test_gcd(25.25, 15.
test_gcd(3.16, 3)
```

The above Python script defines a function called `greatest_common_divisor` that calculates the greatest common divisor of two numbers. The function uses the loop to find the greatest common divisor and returns the result.